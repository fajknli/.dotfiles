#!/usr/bin/env python3

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2026-03-24 21:10


# -*- coding: utf-8 -*-
"""
RST 笔记 RAG 系统 v4.0 - 修复卡死和自动循环问题
修复：进程清理、输入流、重复生成
"""

import os
import sys
import pickle
import json
import subprocess
import signal
import threading
import time
from pathlib import Path
from queue import Queue, Empty

import numpy as np
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
import torch

# ==================== 配置区域 ====================
NOTES_ROOT = os.path.expanduser("~/Documents/Notes")
CACHE_FILE = os.path.expanduser("~/Documents/Notes/.e5_index_cache.pkl")
MODEL_NAME = "intfloat/multilingual-e5-large"

# llama.cpp 路径
LLAMA_CPP_BIN = os.path.expanduser("~/Public/ai/llama.cpp/build/bin")
LLM_MODEL = os.path.expanduser("~/.cache/llama.cpp/Jackrong_Qwen3.5-2B-Claude-4.6-Opus-Reasoning-Distilled-GGUF_Qwen3.5-2B.Q4_K_M.gguf")

# 分块配置
MIN_CHUNK = 150
TARGET_CHUNK = 350
MAX_CHUNK = 500
OVERLAP = 60

# LLM 配置
class Config:
    LLM_MAX_TOKENS = 512          # 减少 token 数，加快生成
    LLM_TEMPERATURE = 0.5         # 降低随机性
    LLM_GPU_LAYERS = 0            # 0=纯 CPU
    LLM_TOP_K = 3
    LLM_TIMEOUT = 60              # 减少超时时间
    LLM_RETRY = 1                 # 减少重试

# ================================================


class TimeoutError(Exception):
    pass


class LLMGenerator:
    """LLM 答案生成器（修复进程清理）"""

    _instance = None  # 单例模式，避免重复加载

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, model_path=LLM_MODEL):
        # 单例模式，只初始化一次
        if hasattr(self, '_initialized') and self._initialized:
            return

        if not os.path.exists(model_path):
            raise FileNotFoundError(f"LLM 模型不存在：{model_path}")

        self.model_path = model_path
        self.llama_cli = os.path.join(LLAMA_CPP_BIN, "llama-cli")

        if not os.path.exists(self.llama_cli):
            raise FileNotFoundError(f"llama-cli 不存在：{self.llama_cli}")

        # 检测模型类型
        model_name = os.path.basename(model_path).lower()
        if 'qwen3' in model_name or 'qwen3.5' in model_name:
            self.template = 'qwen3'
        elif 'qwen' in model_name:
            self.template = 'qwen2'
        else:
            self.template = 'chatml'

        self._initialized = True
        print(f"🤖 LLM 模型已加载：{os.path.basename(model_path)}")

    def _format_prompt(self, prompt, system_prompt):
        if self.template == 'qwen3':
            chat = f"<|im_start|>system\n{system_prompt}<|im_end|>\n"
            chat += f"<|im_start|>user\n{prompt}<|im_end|>\n"
            chat += "<|im_start|>assistant\n"
        elif self.template == 'qwen2':
            chat = f"<|im_start|>system\n{system_prompt}<|im_end|>\n"
            chat += f"<|im_start|>user\n{prompt}<|im_end|>\n"
            chat += "<|im_start|>assistant\n"
        else:
            chat = f"<|im_start|>system\n{system_prompt}<|im_end|>\n"
            chat += f"<|im_start|>user\n{prompt}<|im_end|>\n"
            chat += "<|im_start|>assistant\n"
        return chat

    def _run_with_timeout(self, cmd, timeout):
        """修复：正确清理 subprocess 进程"""
        process = None
        try:
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdin=subprocess.DEVNULL,  # ⚠️ 关键：不继承 stdin
                text=True,
                bufsize=1,
                start_new_session=True  # ⚠️ 关键：新进程组，方便清理
            )

            output_queue = Queue()
            error_queue = Queue()

            def read_stream(stream, queue):
                try:
                    for line in iter(stream.readline, ''):
                        queue.put(line)
                finally:
                    stream.close()

            stdout_thread = threading.Thread(target=read_stream, args=(process.stdout, output_queue))
            stderr_thread = threading.Thread(target=read_stream, args=(process.stderr, error_queue))
            stdout_thread.daemon = True
            stderr_thread.daemon = True
            stdout_thread.start()
            stderr_thread.start()

            output_lines = []
            start_time = time.time()

            while process.poll() is None:
                elapsed = time.time() - start_time
                if elapsed > timeout:
                    # 清理整个进程组
                    os.killpg(os.getpgid(process.pid), signal.SIGTERM)
                    process.wait(timeout=5)
                    raise TimeoutError(f"LLM 生成超时 ({timeout}秒)")

                try:
                    while True:
                        line = output_queue.get_nowait()
                        output_lines.append(line)
                        print(line.rstrip(), end='', flush=True)
                except Empty:
                    pass

                time.sleep(0.1)

            stdout_thread.join(timeout=1)
            stderr_thread.join(timeout=1)

            # 确保进程完全结束
            if process.poll() is None:
                process.terminate()
                process.wait(timeout=5)

            return ''.join(output_lines), '', process.returncode

        finally:
            # 确保资源清理
            if process and process.poll() is None:
                try:
                    os.killpg(os.getpgid(process.pid), signal.SIGTERM)
                except:
                    process.kill()
                process.wait(timeout=5)

    def generate(self, prompt, system_prompt="你是一个有帮助的助手，基于提供的笔记内容回答问题。"):
        chat = self._format_prompt(prompt, system_prompt)

        cmd = [
            self.llama_cli,
            "-m", self.model_path,
            "-p", chat,
            "-n", str(Config.LLM_MAX_TOKENS),
            "--temp", str(Config.LLM_TEMPERATURE),
            "-ngl", str(Config.LLM_GPU_LAYERS),
            "--no-display-prompt"
        ]

        for attempt in range(Config.LLM_RETRY + 1):
            try:
                print(f"\n🤖 生成中...\n", flush=True)
                output, error, returncode = self._run_with_timeout(cmd, Config.LLM_TIMEOUT)

                if returncode == 0:
                    return output.strip()
                else:
                    raise RuntimeError(f"返回码 {returncode}")

            except TimeoutError as e:
                print(f"\n⚠️ 尝试 {attempt+1}/{Config.LLM_RETRY+1} 超时")
                if attempt == Config.LLM_RETRY:
                    raise
                time.sleep(1)

            except Exception as e:
                print(f"\n⚠️ 尝试 {attempt+1}/{Config.LLM_RETRY+1} 失败：{e}")
                if attempt == Config.LLM_RETRY:
                    raise
                time.sleep(1)

        return ""


class RstNoteRAG:
    def __init__(self, model_name=MODEL_NAME):
        print(f"🔍 加载嵌入模型：{model_name} ...")
        self.model = SentenceTransformer(model_name)
        self.notes = []
        self.embeddings = None
        self.llm = None

    def init_llm(self):
        if self.llm is None:
            self.llm = LLMGenerator()

    def _is_rst_heading_underline(self, line):
        if len(line) < 3:
            return False
        stripped = line.strip()
        if not all(c in '=-~^`*#"' for c in stripped):
            return False
        if len(set(stripped)) != 1:
            return False
        return True

    def _split_by_headings(self, content):
        sections = []
        lines = content.splitlines()
        current_section = []

        i = 0
        while i < len(lines):
            line = lines[i]
            if self._is_rst_heading_underline(line) and current_section:
                prev_line = current_section[-1] if current_section else ""
                if prev_line.strip() and not prev_line.strip().startswith('..'):
                    sections.append("\n".join(current_section))
                    current_section = []
            current_section.append(line)
            i += 1

        if current_section:
            sections.append("\n".join(current_section))
        return sections

    def _chunk_with_overlap(self, text, chunk_size=TARGET_CHUNK, overlap=OVERLAP):
        if len(text) <= chunk_size:
            return [text]

        chunks = []
        lines = text.splitlines()
        current_chunk = []
        current_len = 0

        for line in lines:
            current_chunk.append(line)
            current_len += len(line) + 1

            if current_len >= chunk_size:
                chunks.append("\n".join(current_chunk))
                if overlap > 0 and len(current_chunk) > overlap:
                    current_chunk = current_chunk[-overlap:]
                    current_len = sum(len(l) + 1 for l in current_chunk)
                else:
                    current_chunk = []
                    current_len = 0

        if current_chunk:
            chunks.append("\n".join(current_chunk))
        return chunks

    def smart_chunk_rst(self, content, file_path=""):
        chunks = []
        sections = self._split_by_headings(content)

        for section in sections:
            section_len = len(section)
            title = "Untitled"
            for line in section.splitlines():
                if line.strip() and not line.strip().startswith('..'):
                    if not self._is_rst_heading_underline(line):
                        title = line.strip()[:50]
                        break

            if section_len < MIN_CHUNK:
                continue
            elif section_len <= MAX_CHUNK:
                chunks.append((section, title))
            else:
                sub_chunks = self._chunk_with_overlap(section, TARGET_CHUNK, OVERLAP)
                for i, sub in enumerate(sub_chunks):
                    sub_title = f"{title} ({i+1}/{len(sub_chunks)})"
                    chunks.append((sub, sub_title))

        return chunks

    def _clean_rst_content(self, content):
        lines = content.splitlines()
        cleaned = []

        for line in lines:
            if self._is_rst_heading_underline(line):
                continue
            if line.strip().startswith('.. ') and '::' in line:
                continue
            if line.strip() == '' and cleaned and cleaned[-1].strip() == '':
                continue
            cleaned.append(line)

        return "\n".join(cleaned)

    def load_rst_files(self, root_dir):
        rst_files = []

        for dirpath, dirnames, filenames in os.walk(root_dir):
            if 'build' in dirpath or '__pycache__' in dirpath:
                continue
            if any(p.startswith('.') for p in dirpath.split(os.sep)):
                continue

            for filename in filenames:
                if filename.endswith('.rst'):
                    rst_files.append(os.path.join(dirpath, filename))

        print(f"📂 找到 {len(rst_files)} 个 .rst 文件")

        total_chunks = 0
        for file_path in rst_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    content = self._clean_rst_content(content)
                    chunks = self.smart_chunk_rst(content, file_path)

                    for chunk_content, chunk_title in chunks:
                        if len(chunk_content) > MIN_CHUNK:
                            rel_path = os.path.relpath(file_path, start=root_dir)
                            self.notes.append({
                                "file": file_path,
                                "rel_path": rel_path,
                                "title": chunk_title,
                                "content": chunk_content
                            })
                            total_chunks += 1

            except Exception as e:
                print(f"⚠️ 读取失败 {file_path}: {e}")

        print(f"✅ 成功加载 {len(rst_files)} 个文件，分块为 {total_chunks} 个片段")

    def build_index(self):
        if not self.notes:
            print("❌ 没有笔记可索引")
            return False

        texts = [f"passage: {note['title']} - {note['content']}" for note in self.notes]

        print(f"🔧 正在生成 {len(texts)} 个向量索引...")
        self.embeddings = self.model.encode(
            texts,
            normalize_embeddings=True,
            show_progress_bar=True,
            batch_size=32
        )
        print("✅ 索引构建完成")
        return True

    def save_cache(self, cache_file=CACHE_FILE):
        try:
            with open(cache_file, "wb") as f:
                pickle.dump({
                    "notes": self.notes,
                    "embeddings": self.embeddings,
                    "model_name": MODEL_NAME
                }, f)
            print(f"💾 索引缓存已保存：{cache_file}")
            return True
        except Exception as e:
            print(f"⚠️ 缓存保存失败：{e}")
            return False

    def load_cache(self, cache_file=CACHE_FILE):
        if not os.path.exists(cache_file):
            return False

        try:
            with open(cache_file, "rb") as f:
                data = pickle.load(f)
                self.notes = data["notes"]
                self.embeddings = data["embeddings"]

                if data.get("model_name") != MODEL_NAME:
                    print("⚠️ 缓存模型版本不一致，建议重建索引")

                print(f"📦 已从缓存加载 {len(self.notes)} 个片段")
                return True
        except Exception as e:
            print(f"⚠️ 缓存加载失败：{e}")
            return False

    def search(self, query, top_k=5):
        if self.embeddings is None:
            print("❌ 请先构建索引")
            return []

        q_emb = self.model.encode(f"query: {query}", normalize_embeddings=True)
        scores = cos_sim(q_emb, self.embeddings)[0]

        top_indices = torch.topk(scores, k=min(top_k, len(scores))).indices

        results = []
        for idx in top_indices:
            idx = int(idx)
            results.append({
                "file": self.notes[idx]["file"],
                "rel_path": self.notes[idx]["rel_path"],
                "title": self.notes[idx]["title"],
                "content": self.notes[idx]["content"],
                "score": float(scores[idx])
            })
        return results

    def generate_answer(self, query, results):
        self.init_llm()

        context_parts = []
        for i, res in enumerate(results, 1):
            context_parts.append(f"""【来源 {i}】{res['title']}
文件：{res['rel_path']}
内容：
{res['content'][:600]}
---""")

        context = "\n\n".join(context_parts)

        prompt = f"""请基于以下笔记内容回答用户问题。

【笔记内容】
{context}

【用户问题】
{query}

【回答要求】
1. 基于笔记内容回答，不要编造信息
2. 如果笔记中没有相关信息，请明确说明
3. 引用来源时注明文件路径
4. 用简洁清晰的中文回答

【回答】
"""

        answer = self.llm.generate(prompt)
        return answer

    def clear_cache(self, cache_file=CACHE_FILE):
        if os.path.exists(cache_file):
            os.remove(cache_file)
            print(f"🗑️ 缓存已清除：{cache_file}")


# ==================== 信号处理 ====================
def signal_handler(sig, frame):
    print("\n\n⚠️ 检测到中断，正在退出...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)


# ==================== 主程序 ====================
if __name__ == "__main__":
    # 确保标准输入输出可用
    sys.stdin.reconfigure(encoding='utf-8')
    sys.stdout.reconfigure(encoding='utf-8')

    print("="*70)
    print("📚 RST 笔记 RAG 系统 v4.0 (修复卡死版)")
    print("   嵌入模型：intfloat/multilingual-e5-large")
    print(f"   LLM 模型：{os.path.basename(LLM_MODEL)}")
    print(f"   GPU 层数：{Config.LLM_GPU_LAYERS} (0=纯 CPU)")
    print("="*70)

    if not os.path.exists(NOTES_ROOT):
        print(f"❌ 目录不存在：{NOTES_ROOT}")
        sys.exit(1)

    print(f"📁 笔记根目录：{NOTES_ROOT}")

    rag = RstNoteRAG()

    print()
    if rag.load_cache():
        print("✅ 使用缓存索引")
    else:
        print("🔨 首次运行，正在构建索引...")
        rag.load_rst_files(NOTES_ROOT)

        if not rag.notes:
            print("❌ 未加载到任何笔记")
            sys.exit(1)

        if rag.build_index():
            rag.save_cache()

    print("\n" + "="*70)
    print("🎉 RAG 系统就绪！")
    print("   输入问题开始问答")
    print("   命令：'q' 退出，'clear' 清除缓存")
    print("         'cpu' 切换纯 CPU，'gpu' 切换 GPU(12 层)")
    print("         'search' 仅检索模式")
    print("   提示：卡住可按 Ctrl+C 中断")
    print("="*70)

    # 主循环
    while True:
        try:
            # 清空输入缓冲
            sys.stdout.flush()

            query = input("\n🤔 问题：")

            # 清空输入缓冲，防止污染
            query = query.strip()

        except (EOFError, KeyboardInterrupt):
            print("\n👋 再见！")
            break

        if not query:
            continue

        cmd = query.lower()

        # 命令处理
        if cmd in ['q', 'quit', 'exit']:
            print("👋 再见！")
            break
        elif cmd == 'clear':
            rag.clear_cache()
            continue
        elif cmd == 'cpu':
            Config.LLM_GPU_LAYERS = 0
            print("✅ 已切换到纯 CPU 模式")
            continue
        elif cmd == 'gpu':
            Config.LLM_GPU_LAYERS = 12
            print("✅ 已切换到 GPU 模式 (12 层)")
            continue
        elif cmd == 'search':
            print("💡 仅检索模式，输入查询词...")
            search_query = input("🔍 查询：").strip()
            if search_query:
                results = rag.search(search_query, top_k=5)
                for i, res in enumerate(results, 1):
                    print(f"{i}. [{res['score']:.4f}] {res['title']} - {res['rel_path']}")
            continue

        # 1. 检索
        print("\n🔍 检索相关笔记...")
        results = rag.search(query, top_k=Config.LLM_TOP_K)

        if not results:
            print("   ⚠️ 未找到相关笔记")
            continue

        # 显示检索结果
        print(f"\n📌 找到 {len(results)} 篇相关笔记：")
        for i, res in enumerate(results, 1):
            print(f"   {i}. [{res['score']:.4f}] {res['title']}")
            print(f"      📁 {res['rel_path']}")

        # 2. 明确询问是否生成（避免自动循环）
        print()
        gen_input = input("💬 是否生成答案？输入 'y' 生成，其他跳过：").strip().lower()

        if gen_input == 'y':
            print("\n" + "-"*70)
            try:
                answer = rag.generate_answer(query, results)
                print("\n" + "="*70)
                print("💡 答案：")
                print("="*70)
                print(answer)
                print("="*70)
            except Exception as e:
                print(f"\n❌ 生成失败：{e}")
                print("💡 建议：输入 'cpu' 切换到纯 CPU 模式")
            finally:
                # 确保生成后回到主循环
                print()
        else:
            print("⏭️ 已跳过答案生成，继续查询...")
