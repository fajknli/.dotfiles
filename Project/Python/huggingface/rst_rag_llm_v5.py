#!/usr/bin/env python3
# Author:       fajknli
# Email:        fajknli@gmail.com
# Created:      2026-03-24
# Version:      5.0 - 多轮对话 / MMR去重 / 相关性过滤 / 流式输出 / 持久进程

# -*- coding: utf-8 -*-
"""
RST 笔记 RAG 系统 v5.0
改进：
  1. MMR 检索去重（最大边际相关性）
  2. 相关性阈值过滤（低质量结果不送 LLM）
  3. 多轮对话上下文（保留最近 N 轮）
  4. 流式输出（逐字打印，而非等待完成）
  5. 索引元数据统计（大小/时间）
  6. 更安全的进程清理
  7. 文件日志支持
  8. 命令行参数（--rebuild / --search-only / --no-llm）
"""

import os
import sys
import pickle
import json
import subprocess
import signal
import threading
import time
import logging
import argparse
from datetime import datetime
from pathlib import Path
from queue import Queue, Empty

import numpy as np
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
import torch

# ==================== 配置区域 ====================
NOTES_ROOT   = os.path.expanduser("~/Documents/Notes"
CACHE_FILE   = os.path.expanduser("~/Documents/Notes/.e5_index_cache.pkl")
LOG_FILE     = os.path.expanduser("~/Documents/Notes/.rag_v5.log")
MODEL_NAME   = "intfloat/multilingual-e5-large"

LLAMA_CPP_BIN = os.path.expanduser("~/Public/ai/llama.cpp/build/bin")
LLM_MODEL     = os.path.expanduser(
    "~/.cache/llama.cpp/"
    "Jackrong_Qwen3.5-2B-Claude-4.6-Opus-Reasoning-Distilled-GGUF_"
    "Qwen3.5-2B.Q4_K_M.gguf"
)

# 分块配置
MIN_CHUNK    = 150
TARGET_CHUNK = 350
MAX_CHUNK    = 500
OVERLAP      = 60


class Config:
    LLM_MAX_TOKENS  = 512
    LLM_TEMPERATURE = 0.5
    LLM_GPU_LAYERS  = 0          # 0 = 纯 CPU
    LLM_TOP_K       = 3          # 检索 top-k
    LLM_TIMEOUT     = 60
    LLM_RETRY       = 1

    # ── 新增 ──────────────────────────────────────
    SCORE_THRESHOLD  = 0.30      # 相关性最低阈值，低于此分数丢弃
    MMR_LAMBDA       = 0.6       # MMR 多样性权重（0=全多样, 1=全相关）
    MAX_HISTORY      = 4         # 对话历史保留轮数（用户+助手各算1轮）
    STREAM_DELAY     = 0.0       # 流式输出每字间隔（0 = 不限速）
# =================================================


# ==================== 日志 =======================
def setup_logging(log_file: str, verbose: bool = False):
    level = logging.DEBUG if verbose else logging.INFO
    handlers = [logging.StreamHandler(sys.stderr)]
    try:
        handlers.append(logging.FileHandler(log_file, encoding="utf-8"))
    except Exception as e:
    logging.warning(f"无法写入日志文件: {e}")

    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=handlers,
    )

log = logging.getLogger("RAG")
# =================================================


class TimeoutError(Exception):
    pass


# ─────────────────────────────────────────────────
#  MMR 检索去重
# ─────────────────────────────────────────────────
def mmr_rerank(
    query_emb: np.ndarray,
    candidate_embs: np.ndarray,
    candidate_indices: list[int],
    top_k: int,
    lambda_param: float = Config.MMR_LAMBDA,
) -> list[int]:
    """
    Maximum Marginal Relevance
    返回 top_k 个索引（从 candidate_indices 中挑选）
    """
    if len(candidate_indices) <= top_k:
        return candidate_indices

    query_emb = np.array(query_emb)
    selected: list[int] = []
    remaining = list(candidate_indices)

    # 预计算查询相关性
    rel_scores = {}
    for idx in remaining:
        sim = float(np.dot(query_emb, candidate_embs[idx]))
        rel_scores[idx] = sim

    while len(selected) < top_k and remaining:
        if not selected:
            # 第一轮：选相关性最高的
            best = max(remaining, key=lambda i: rel_scores[i])
        else:
            # 后续轮：MMR 分数
            sel_embs = candidate_embs[selected]  # shape (S, D)
            best, best_score = None, -np.inf
            for idx in remaining:
                emb = candidate_embs[idx]
                max_sim_to_selected = float(np.max(sel_embs @ emb))
                mmr_score = (
                    lambda_param * rel_scores[idx]
                    - (1 - lambda_param) * max_sim_to_selected
                )
                if mmr_score > best_score:
                    best_score = mmr_score
                    best = idx

        selected.append(best)
        remaining.remove(best)

    return selected


# ─────────────────────────────────────────────────
#  LLM 生成器
# ─────────────────────────────────────────────────
class LLMGenerator:
    """llama.cpp 子进程封装（流式输出 + 安全清理）"""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, model_path: str = LLM_MODEL):
        if getattr(self, "_initialized", False):
            return

        if not os.path.exists(model_path):
            raise FileNotFoundError(f"LLM 模型不存在：{model_path}")

        self.model_path = model_path
        self.llama_cli  = os.path.join(LLAMA_CPP_BIN, "llama-cli")

        if not os.path.exists(self.llama_cli):
            raise FileNotFoundError(f"llama-cli 不存在：{self.llama_cli}")

        name = os.path.basename(model_path).lower()
        if "qwen3" in name:
            self.template = "qwen3"
        elif "qwen" in name:
            self.template = "qwen2"
        else:
            self.template = "chatml"

        self._initialized = True
        log.info(f"LLM 已加载：{os.path.basename(model_path)}")

    def _format_prompt(
        self,
        messages: list[dict],    # [{"role": "user"|"assistant", "content": "..."}]
        system_prompt: str,
    ) -> str:
        """将多轮对话格式化为模板字符串"""
        chat = f"<|im_start|>system\n{system_prompt}<|im_end|>\n"
        for msg in messages:
            chat += f"<|im_start|>{msg['role']}\n{msg['content']}<|im_end|>\n"
        chat += "<|im_start|>assistant\n"
        return chat

    def _kill_process(self, process):
        """安全清理子进程"""
        if process is None or process.poll() is not None:
            return
        try:
            pgid = os.getpgid(process.pid)
            os.killpg(pgid, signal.SIGTERM)
        except (ProcessLookupError, OSError):
            try:
                process.terminate()
            except Exception:
                pass
        try:
            process.wait(timeout=5)
        except Exception:
            try:
                process.kill()
            except Exception:
                pass

    def _run_streaming(self, cmd: list[str], timeout: int):
        """
        运行子进程并流式打印输出。
        返回 (full_output: str, returncode: int)
        """
        process = None
        try:
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,   # 静默 stderr（避免干扰输出）
                stdin=subprocess.DEVNULL,
                text=True,
                bufsize=1,
                start_new_session=True,
            )

            output_parts: list[str] = []
            start = time.time()

            # 逐字符读取，实现流式效果
            while True:
                if process.poll() is not None:
                    # 进程结束，读取剩余输出
                    rest = process.stdout.read()
                    if rest:
                        print(rest, end="", flush=True)
                        output_parts.append(rest)
                    break

                if time.time() - start > timeout:
                    self._kill_process(process)
                    raise TimeoutError(f"LLM 超时（{timeout}s）")

                char = process.stdout.read(1)
                if char:
                    print(char, end="", flush=True)
                    output_parts.append(char)
                    if Config.STREAM_DELAY:
                        time.sleep(Config.STREAM_DELAY)
                else:
                    time.sleep(0.02)

            rc = process.wait(timeout=5)
            return "".join(output_parts).strip(), rc

        finally:
            self._kill_process(process)

    def generate(
        self,
        messages: list[dict],
        system_prompt: str = "你是一个有帮助的助手，基于提供的笔记内容回答问题。",
    ) -> str:
        chat = self._format_prompt(messages, system_prompt)

        cmd = [
            self.llama_cli,
            "-m", self.model_path,
            "-p", chat,
            "-n", str(Config.LLM_MAX_TOKENS),
            "--temp", str(Config.LLM_TEMPERATURE),
            "-ngl", str(Config.LLM_GPU_LAYERS),
            "--no-display-prompt",
        ]

        for attempt in range(Config.LLM_RETRY + 1):
            try:
                print(f"\n🤖 生成中...\n{'─'*50}", flush=True)
                output, rc = self._run_streaming(cmd, Config.LLM_TIMEOUT)
                print()  # 换行
                if rc == 0:
                    return output
                raise RuntimeError(f"llama-cli 返回码 {rc}")

            except TimeoutError as e:
                log.warning(f"尝试 {attempt+1}/{Config.LLM_RETRY+1}：{e}")
                if attempt == Config.LLM_RETRY:
                    raise
                time.sleep(1)

            except Exception as e:
                log.warning(f"尝试 {attempt+1}/{Config.LLM_RETRY+1}：{e}")
                if attempt == Config.LLM_RETRY:
                    raise
                time.sleep(1)

        return ""


# ─────────────────────────────────────────────────
#  RST 解析 & RAG 核心
# ─────────────────────────────────────────────────
class RstNoteRAG:
    def __init__(self, model_name: str = MODEL_NAME):
        log.info(f"加载嵌入模型：{model_name}")
        print(f"🔍 加载嵌入模型：{model_name} ...")
        self.model      = SentenceTransformer(model_name)
        self.notes: list[dict]     = []
        self.embeddings: np.ndarray | None = None
        self.llm: LLMGenerator | None      = None

        # 多轮对话历史：[{"role": "user"|"assistant", "content": "..."}]
        self.history: list[dict] = []

    # ── 初始化 LLM ────────────────────────────────
    def init_llm(self):
        if self.llm is None:
            self.llm = LLMGenerator()

    # ── RST 工具方法 ──────────────────────────────
    def _is_heading_underline(self, line: str) -> bool:
        stripped = line.strip()
        return (
            len(stripped) >= 3
            and all(c in "=-~^`*#\"" for c in stripped)
            and len(set(stripped)) == 1
        )

    def _split_by_headings(self, content: str) -> list[str]:
        sections, current = [], []
        for line in content.splitlines():
            if self._is_heading_underline(line) and current:
                if current[-1].strip():
                    sections.append("\n".join(current))
                    current = []
            current.append(line)
        if current:
            sections.append("\n".join(current))
        return sections

    def _chunk_with_overlap(
        self, text: str, chunk_size: int = TARGET_CHUNK, overlap: int = OVERLAP
    ) -> list[str]:
        if len(text) <= chunk_size:
            return [text]

        chunks, current, current_len = [], [], 0
        for line in text.splitlines():
            current.append(line)
            current_len += len(line) + 1
            if current_len >= chunk_size:
                chunks.append("\n".join(current))
                tail = current[-overlap:] if overlap and len(current) > overlap else []
                current = tail
                current_len = sum(len(l) + 1 for l in current)
        if current:
            chunks.append("\n".join(current))
        return chunks

    def _clean_rst(self, content: str) -> str:
        lines, cleaned = content.splitlines(), []
        for line in lines:
            if self._is_heading_underline(line):
                continue
            if line.strip().startswith(".. ") and "::" in line:
                continue
            if not line.strip() and cleaned and not cleaned[-1].strip():
                continue
            cleaned.append(line)
        return "\n".join(cleaned)

    def _smart_chunk(self, content: str) -> list[tuple[str, str]]:
        chunks = []
        for section in self._split_by_headings(content):
            title = "Untitled"
            for l in section.splitlines():
                if l.strip() and not l.strip().startswith("..") and not self._is_heading_underline(l):
                    title = l.strip()[:50]
                    break

            slen = len(section)
            if slen < MIN_CHUNK:
                continue
            elif slen <= MAX_CHUNK:
                chunks.append((section, title))
            else:
                subs = self._chunk_with_overlap(section)
                for i, s in enumerate(subs):
                    chunks.append((s, f"{title} ({i+1}/{len(subs)})"))
        return chunks

    # ── 文件加载 ──────────────────────────────────
    def load_rst_files(self, root_dir: str):
        rst_files = [
            str(p)
            for p in Path(root_dir).rglob("*.rst")
            if not any(part.startswith(".") or part in ("build", "__pycache__")
                       for part in p.parts)
        ]
        print(f"📂 找到 {len(rst_files)} 个 .rst 文件")

        for fp in rst_files:
            try:
                content = self._clean_rst(Path(fp).read_text(encoding="utf-8"))
                for chunk, title in self._smart_chunk(content):
                    if len(chunk) > MIN_CHUNK:
                        self.notes.append({
                            "file":     fp,
                            "rel_path": os.path.relpath(fp, root_dir),
                            "title":    title,
                            "content":  chunk,
                        })
            except Exception as e:
                log.warning(f"读取失败 {fp}: {e}")

        print(f"✅ 加载完成：{len(rst_files)} 个文件 → {len(self.notes)} 个片段")

    # ── 索引 ──────────────────────────────────────
    def build_index(self) -> bool:
        if not self.notes:
            print("❌ 没有笔记可索引")
            return False

        texts = [f"passage: {n['title']} - {n['content']}" for n in self.notes]
        print(f"🔧 生成 {len(texts)} 个向量...")
        self.embeddings = self.model.encode(
            texts, normalize_embeddings=True,
            show_progress_bar=True, batch_size=32
        )
        print("✅ 索引构建完成")
        return True

    def save_cache(self, cache_file: str = CACHE_FILE) -> bool:
        try:
            with open(cache_file, "wb") as f:
                pickle.dump({
                    "notes":      self.notes,
                    "embeddings": self.embeddings,
                    "model_name": MODEL_NAME,
                    "built_at":   datetime.now().isoformat(),
                }, f)
            size_mb = os.path.getsize(cache_file) / 1024 / 1024
            print(f"💾 缓存已保存：{cache_file} ({size_mb:.1f} MB)")
            return True
        except Exception as e:
            log.warning(f"缓存保存失败：{e}")
            return False

    def load_cache(self, cache_file: str = CACHE_FILE) -> bool:
        if not os.path.exists(cache_file):
            return False
        try:
            with open(cache_file, "rb") as f:
                data = pickle.load(f)
            self.notes      = data["notes"]
            self.embeddings = data["embeddings"]

            if data.get("model_name") != MODEL_NAME:
                print("⚠️ 缓存模型版本不一致，建议重建（输入 'rebuild'）")

            built_at = data.get("built_at", "未知")
            size_mb  = os.path.getsize(cache_file) / 1024 / 1024
            print(f"📦 缓存加载：{len(self.notes)} 片段 | 构建时间：{built_at} | {size_mb:.1f} MB")
            return True
        except Exception as e:
            log.warning(f"缓存加载失败：{e}")
            return False

    def clear_cache(self, cache_file: str = CACHE_FILE):
        if os.path.exists(cache_file):
            os.remove(cache_file)
            print(f"🗑️ 缓存已清除：{cache_file}")

    # ── 检索（含 MMR + 阈值过滤）─────────────────
    def search(
        self,
        query: str,
        top_k: int = None,
        use_mmr: bool = True,
    ) -> list[dict]:
        if self.embeddings is None:
            print("❌ 请先构建索引")
            return []

        if top_k is None:
            top_k = Config.LLM_TOP_K

        q_emb = self.model.encode(f"query: {query}", normalize_embeddings=True)
        scores = cos_sim(q_emb, self.embeddings)[0].numpy()

        # 阈值过滤
        candidate_idx = [
            i for i, s in enumerate(scores)
            if s >= Config.SCORE_THRESHOLD
        ]

        if not candidate_idx:
            # 阈值无匹配时退回全量 top-k（降级处理）
            candidate_idx = torch.topk(
                torch.tensor(scores), k=min(top_k * 3, len(scores))
            ).indices.tolist()
            log.info("所有结果低于阈值，已降级为全量 top-k")

        # 取分数最高的 top_k*3 做 MMR 候选池
        pool = sorted(candidate_idx, key=lambda i: scores[i], reverse=True)[:top_k * 3]

        if use_mmr and len(pool) > top_k:
            selected = mmr_rerank(q_emb, self.embeddings, pool, top_k)
        else:
            selected = pool[:top_k]

        return [
            {
                **self.notes[i],
                "score": float(scores[i]),
            }
            for i in selected
        ]

    # ── 多轮对话生成 ──────────────────────────────
    def generate_answer(
        self,
        query: str,
        results: list[dict],
        no_llm: bool = False,
    ) -> str:
        if no_llm:
            return "（--no-llm 模式，跳过生成）"

        self.init_llm()

        context = "\n\n".join(
            f"【来源 {i}】{r['title']}\n文件：{r['rel_path']}\n"
            f"内容：\n{r['content'][:600]}\n---"
            for i, r in enumerate(results, 1)
        )

        system_prompt = (
            "你是一个严谨的知识助手，只基于用户提供的笔记内容回答问题。\n"
            "如果笔记中没有相关信息，请明确说明'未找到相关内容'，不要编造。\n"
            "引用信息时注明来源文件路径。用简洁清晰的中文回答。"
        )

        # 构造当前轮用户消息（含上下文）
        user_content = (
            f"【参考笔记】\n{context}\n\n"
            f"【问题】{query}"
        )

        # 拼接历史 + 当前轮
        messages = self.history[-Config.MAX_HISTORY * 2:] + [
            {"role": "user", "content": user_content}
        ]

        answer = self.llm.generate(messages, system_prompt)

        # 更新历史（保留简化版，不含上下文块）
        self.history.append({"role": "user",      "content": query})
        self.history.append({"role": "assistant", "content": answer})
        if len(self.history) > Config.MAX_HISTORY * 2:
            self.history = self.history[-Config.MAX_HISTORY * 2:]

        return answer

    def clear_history(self):
        self.history.clear()
        print("🗑️ 对话历史已清除")


# ==================== 信号处理 ====================
def _sig_handler(sig, frame):
    print("\n\n⚠️ 中断，正在退出...")
    sys.exit(0)

signal.signal(signal.SIGINT, _sig_handler)
signal.signal(signal.SIGTERM, _sig_handler)


# ==================== CLI ==========================
def parse_args():
    parser = argparse.ArgumentParser(description="RST 笔记 RAG 系统 v5.0")
    parser.add_argument("--rebuild",     action="store_true", help="强制重建索引")
    parser.add_argument("--search-only", action="store_true", help="只检索，不生成")
    parser.add_argument("--no-llm",      action="store_true", help="禁用 LLM（=search-only）")
    parser.add_argument("--top-k",       type=int,  default=Config.LLM_TOP_K, help="检索数量")
    parser.add_argument("--threshold",   type=float, default=Config.SCORE_THRESHOLD, help="相关性阈值")
    parser.add_argument("--gpu-layers",  type=int,  default=Config.LLM_GPU_LAYERS, help="GPU 卸载层数")
    parser.add_argument("--verbose",     action="store_true", help="显示 DEBUG 日志")
    return parser.parse_args()


# ==================== 主程序 =======================
def main():
    args = parse_args()

    # 应用 CLI 参数
    Config.LLM_TOP_K       = args.top_k
    Config.SCORE_THRESHOLD = args.threshold
    Config.LLM_GPU_LAYERS  = args.gpu_layers
    no_llm = args.no_llm or args.search_only

    setup_logging(LOG_FILE, args.verbose)

    # 修复终端编码
    for stream in (sys.stdin, sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except Exception:
            pass

    banner = f"""
{'='*70}
📚  RST 笔记 RAG 系统 v5.0
    嵌入：{MODEL_NAME}
    LLM ：{os.path.basename(LLM_MODEL)}
    GPU ：{Config.LLM_GPU_LAYERS} 层 | top-k={Config.LLM_TOP_K} | 阈值={Config.SCORE_THRESHOLD}
    MMR ：λ={Config.MMR_LAMBDA} | 历史={Config.MAX_HISTORY} 轮
{'='*70}"""
    print(banner)

    if not os.path.exists(NOTES_ROOT):
        print(f"❌ 目录不存在：{NOTES_ROOT}")
        sys.exit(1)

    rag = RstNoteRAG()

    if args.rebuild or not rag.load_cache():
        print("🔨 构建索引...")
        rag.load_rst_files(NOTES_ROOT)
        if not rag.notes:
            print("❌ 未加载到任何笔记")
            sys.exit(1)
        if rag.build_index():
            rag.save_cache()

    print(f"""
{'='*70}
🎉  RAG 就绪！
    命令：q/quit  退出
          clear   清除索引缓存
          history 查看对话历史
          reset   清空对话历史
          rebuild 重建索引
          cpu     纯 CPU 模式
          gpu     GPU 模式（12层）
          search <词>  仅检索
    提示：Ctrl+C 中断生成
{'='*70}""")

    while True:
        try:
            sys.stdout.flush()
            query = input("\n🤔 问题：").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n👋 再见！")
            break

        if not query:
            continue

        cmd = query.lower()

        # ── 命令处理 ──────────────────────────────
        if cmd in ("q", "quit", "exit"):
            print("👋 再见！")
            break

        elif cmd == "clear":
            rag.clear_cache()
            continue

        elif cmd == "rebuild":
            rag.notes.clear()
            rag.embeddings = None
            rag.load_rst_files(NOTES_ROOT)
            if rag.build_index():
                rag.save_cache()
            continue

        elif cmd == "history":
            if not rag.history:
                print("（无对话历史）")
            for i, m in enumerate(rag.history):
                icon = "🤔" if m["role"] == "user" else "💡"
                print(f"{icon} {m['role']}: {m['content'][:120]}{'…' if len(m['content'])>120 else ''}")
            continue

        elif cmd in ("reset", "clear history"):
            rag.clear_history()
            continue

        elif cmd == "cpu":
            Config.LLM_GPU_LAYERS = 0
            print("✅ 纯 CPU 模式")
            continue

        elif cmd == "gpu":
            Config.LLM_GPU_LAYERS = 12
            print("✅ GPU 模式（12 层）")
            continue

        elif cmd.startswith("search "):
            kw = query[7:].strip()
            if kw:
                results = rag.search(kw, top_k=Config.LLM_TOP_K * 2)
                print(f"\n📌 检索结果（{len(results)} 条）：")
                for i, r in enumerate(results, 1):
                    print(f"   {i}. [{r['score']:.4f}] {r['title']}")
                    print(f"      📁 {r['rel_path']}")
            continue

        # ── RAG 主流程 ────────────────────────────
        print("\n🔍 检索相关笔记...")
        results = rag.search(query)

        if not results:
            print("   ⚠️ 未找到相关笔记（尝试降低阈值：--threshold 0.2）")
            continue

        print(f"\n📌 相关笔记（{len(results)} 条，MMR 去重）：")
        for i, r in enumerate(results, 1):
            flag = "🟢" if r["score"] >= 0.5 else "🟡" if r["score"] >= 0.3 else "🔴"
            print(f"   {i}. {flag} [{r['score']:.4f}] {r['title']}")
            print(f"      📁 {r['rel_path']}")

        if no_llm:
            continue

        gen = input("\n💬 生成答案？[y/N] ").strip().lower()
        if gen != "y":
            print("⏭️ 跳过生成")
            continue

        print(f"\n{'─'*70}")
        try:
            answer = rag.generate_answer(query, results)
            print(f"\n{'='*70}")
            print("💡 答案：")
            print("="*70)
            print(answer)
            print("="*70)
        except TimeoutError:
            print("\n❌ 生成超时，输入 'cpu' 切换到纯 CPU 模式")
        except Exception as e:
            log.error(f"生成失败：{e}", exc_info=True)
            print(f"\n❌ 生成失败：{e}")


if __name__ == "__main__":
    main()
