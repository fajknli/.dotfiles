#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RST 笔记检索系统 - 适配 ~/Documents/Notes 目录结构
支持中英混用查询，基于 intfloat/multilingual-e5-large
功能：智能分块、重叠处理、索引缓存、多标题格式支持
"""

import os
import sys
import pickle
import glob
from pathlib import Path
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
import torch

# ==================== 配置区域 ====================
NOTES_ROOT = os.path.expanduser("~/Documents/Notes")
CACHE_FILE = os.path.expanduser("~/Documents/Notes/.e5_index_cache.pkl")
MODEL_NAME = "intfloat/multilingual-e5-large"

# 分块配置
MIN_CHUNK = 150       # 最小块长度（字符数）
TARGET_CHUNK = 350    # 目标块长度
MAX_CHUNK = 500       # 最大块长度（不超过 512 tokens）
OVERLAP = 60          # 重叠长度（字符数）
# ================================================


class RstNoteRAG:
    def __init__(self, model_name=MODEL_NAME):
        print(f"🔍 加载模型：{model_name} ...")
        self.model = SentenceTransformer(model_name)
        self.notes = []
        self.embeddings = None

    def _is_rst_heading_underline(self, line):
        """
        检测 reST 标题装饰线
        支持：====、----、''''''、~~~~、^^^^、#### 等
        """
        if len(line) < 3:
            return False
        stripped = line.strip()
        # 必须是纯装饰字符组成
        if not all(c in '=-~^`*#"' for c in stripped):
            return False
        # 装饰字符必须重复至少 3 次
        if len(set(stripped)) != 1:
            return False
        return True

    def _split_by_headings(self, content):
        """
        按 reST 标题切分内容
        识别标题文字 + 装饰线的组合
        """
        sections = []
        lines = content.splitlines()
        current_section = []

        i = 0
        while i < len(lines):
            line = lines[i]

            # 检测当前行是否是标题装饰线
            if self._is_rst_heading_underline(line) and current_section:
                # 检查前一行是否是标题文字（非空、非指令）
                prev_line = current_section[-1] if current_section else ""
                if prev_line.strip() and not prev_line.strip().startswith('..'):
                    # 这是一个完整的标题结构，切分
                    sections.append("\n".join(current_section))
                    current_section = []

            current_section.append(line)
            i += 1

        # 添加最后一节
        if current_section:
            sections.append("\n".join(current_section))

        return sections

    def _chunk_with_overlap(self, text, chunk_size=TARGET_CHUNK, overlap=OVERLAP):
        """
        对过长的文本进行固定长度切分 + 重叠
        """
        if len(text) <= chunk_size:
            return [text]

        chunks = []
        lines = text.splitlines()
        current_chunk = []
        current_len = 0

        for line in lines:
            current_chunk.append(line)
            current_len += len(line) + 1  # +1 for newline

            if current_len >= chunk_size:
                chunks.append("\n".join(current_chunk))
                # 保留最后 overlap 行作为下一块的开头
                if overlap > 0 and len(current_chunk) > overlap:
                    current_chunk = current_chunk[-overlap:]
                    current_len = sum(len(l) + 1 for l in current_chunk)
                else:
                    current_chunk = []
                    current_len = 0

        # 添加最后一块
        if current_chunk:
            chunks.append("\n".join(current_chunk))

        return chunks

    def smart_chunk_rst(self, content, file_path=""):
        """
        智能分块：优先按标题，其次按长度
        返回：[(chunk_content, chunk_title), ...]
        """
        chunks = []

        # 第一步：按标题切分
        sections = self._split_by_headings(content)

        for section in sections:
            section_len = len(section)

            # 提取章节标题（第一行非空且非指令）
            title = "Untitled"
            for line in section.splitlines():
                if line.strip() and not line.strip().startswith('..'):
                    if not self._is_rst_heading_underline(line):
                        title = line.strip()[:50]  # 标题截断
                        break

            if section_len < MIN_CHUNK:
                # 太短：跳过（或可合并到相邻块）
                continue
            elif section_len <= MAX_CHUNK:
                # 合适：直接作为一块
                chunks.append((section, title))
            else:
                # 太长：按长度再切分 + 重叠
                sub_chunks = self._chunk_with_overlap(section, TARGET_CHUNK, OVERLAP)
                for i, sub in enumerate(sub_chunks):
                    sub_title = f"{title} ({i+1}/{len(sub_chunks)})"
                    chunks.append((sub, sub_title))

        return chunks

    def _clean_rst_content(self, content):
        """简单清洗 reST 内容"""
        lines = content.splitlines()
        cleaned = []

        for i, line in enumerate(lines):
            # 跳过纯装饰线（标题下划线已用于分块，这里再过滤一次）
            if self._is_rst_heading_underline(line):
                continue

            # 跳过 reST 指令（如 .. toctree:: .. code-block::）
            if line.strip().startswith('.. ') and '::' in line:
                continue

            # 跳过连续空行
            if line.strip() == '' and cleaned and cleaned[-1].strip() == '':
                continue

            cleaned.append(line)

        return "\n".join(cleaned)

    def load_rst_files(self, root_dir):
        """
        加载指定根目录下的所有 .rst 源文件
        自动排除 build/ 目录，只读取 source/ 下的文件
        """
        rst_files = []

        # 递归查找所有 .rst 文件
        for dirpath, dirnames, filenames in os.walk(root_dir):
            # 跳过 build 目录和缓存目录
            if 'build' in dirpath or '__pycache__' in dirpath:
                continue
            # 跳过隐藏目录
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

                    # 清洗内容
                    content = self._clean_rst_content(content)

                    # 智能分块
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
        """构建向量索引"""
        if not self.notes:
            print("❌ 没有笔记可索引")
            return False

        # ⚠️ 关键：给每篇笔记加 passage 前缀
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
        """保存索引缓存"""
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
        """加载索引缓存"""
        if not os.path.exists(cache_file):
            return False

        try:
            with open(cache_file, "rb") as f:
                data = pickle.load(f)
                self.notes = data["notes"]
                self.embeddings = data["embeddings"]

                # 验证模型是否一致
                if data.get("model_name") != MODEL_NAME:
                    print("⚠️ 缓存模型版本不一致，建议重建索引")

                print(f"📦 已从缓存加载 {len(self.notes)} 个片段")
                return True
        except Exception as e:
            print(f"⚠️ 缓存加载失败：{e}")
            return False

    def search(self, query, top_k=5):
        """搜索笔记"""
        if self.embeddings is None:
            print("❌ 请先构建索引")
            return []

        # ⚠️ 关键：查询加 query 前缀
        q_emb = self.model.encode(f"query: {query}", normalize_embeddings=True)
        scores = cos_sim(q_emb, self.embeddings)[0]

        # 获取 top_k
        top_indices = torch.topk(scores, k=min(top_k, len(scores))).indices

        results = []
        for idx in top_indices:
            idx = int(idx)
            results.append({
                "file": self.notes[idx]["file"],
                "rel_path": self.notes[idx]["rel_path"],
                "title": self.notes[idx]["title"],
                "content": self.notes[idx]["content"][:400] + "...",
                "score": float(scores[idx])
            })
        return results

    def clear_cache(self, cache_file=CACHE_FILE):
        """清除缓存"""
        if os.path.exists(cache_file):
            os.remove(cache_file)
            print(f"🗑️ 缓存已清除：{cache_file}")


# ==================== 主程序 ====================
if __name__ == "__main__":
    print("="*70)
    print("📚 RST 笔记检索系统 v2.0")
    print("   模型：intfloat/multilingual-e5-large")
    print("   支持：中英混用查询、智能分块、索引缓存")
    print("="*70)

    # 验证目录
    if not os.path.exists(NOTES_ROOT):
        print(f"❌ 目录不存在：{NOTES_ROOT}")
        print("💡 请确认你的笔记是否在 ~/Documents/Notes")
        sys.exit(1)

    print(f"📁 笔记根目录：{NOTES_ROOT}")

    # 显示子目录
    subdirs = [d for d in os.listdir(NOTES_ROOT)
               if os.path.isdir(os.path.join(NOTES_ROOT, d)) and not d.startswith('.')]
    if subdirs:
        print(f"   子目录：{', '.join(subdirs)}")

    # 1. 初始化 RAG
    rag = RstNoteRAG()

    # 2. 尝试加载缓存
    print()
    if rag.load_cache():
        print("✅ 使用缓存索引（如需重建请删除 .e5_index_cache.pkl）")
    else:
        print("🔨 首次运行，正在构建索引...")
        rag.load_rst_files(NOTES_ROOT)

        if not rag.notes:
            print("❌ 未加载到任何笔记，请检查目录结构")
            print(f"   提示：确保 .rst 文件在 {NOTES_ROOT} 下，且不在 build/ 目录中")
            sys.exit(1)

        if rag.build_index():
            rag.save_cache()

    # 3. 交互式搜索
    print("\n" + "="*70)
    print("🎉 检索系统就绪！")
    print("   💡 支持中英混用查询，如 'Docker 网络配置' 或 'Python list comprehension'")
    print("   输入查询开始搜索")
    print("   输入 'q' 退出，'clear' 清除缓存，'stats' 显示统计")
    print("="*70)

    while True:
        try:
            query = input("\n🔍 查询：")
        except (EOFError, KeyboardInterrupt):
            print("\n👋 再见！")
            break

        cmd = query.strip().lower()
        if cmd in ['q', 'quit', 'exit']:
            print("👋 再见！")
            break
        elif cmd == 'clear':
            rag.clear_cache()
            print("💡 下次启动将重建索引")
            continue
        elif cmd == 'stats':
            print(f"\n📊 统计信息:")
            print(f"   总片段数：{len(rag.notes)}")
            print(f"   向量维度：{rag.embeddings.shape[1] if rag.embeddings is not None else 'N/A'}")
            print(f"   缓存文件：{CACHE_FILE}")
            continue
        elif not query.strip():
            continue

        results = rag.search(query, top_k=5)

        if not results:
            print("   ⚠️ 未找到相关结果")
            continue

        print(f"\n{'排名':<4} {'分数':<8} {'标题'}")
        print("-" * 70)
        for i, res in enumerate(results, 1):
            print(f"{i:<4} {res['score']:.4f}   {res['title']}")
            print(f"       📁 {res['rel_path']}")
            # 显示预览（单行）
            preview = ' '.join(res['content'].split())[:120]
            print(f"       └─ {preview}...")
