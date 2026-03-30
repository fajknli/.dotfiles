#!/usr/bin/env python3

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2026-03-24 04:13


from sentence_transformers import SentenceTransformer

# 指向你下载的本地目录（替换成你的实际路径）
model_path = "/home/fajknli/.cache/huggingface/hub/models--intfloat--multilingual-e5-large/snapshots/0dc5580a448e4284468b8909bae50fa925907bc5"

print("🔍 正在加载模型...")
model = SentenceTransformer(model_path)

print("✅ 模型加载成功！")
print(f"   最大长度：{model.max_seq_length} tokens")
print(f"   向量维度：{model.get_sentence_embedding_dimension()}")
