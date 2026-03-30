#!/usr/bin/env python3

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2026-03-24 04:20


from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

# 加载模型（自动使用缓存）
model = SentenceTransformer("intfloat/multilingual-e5-large")

print("🔍 测试中英混用检索效果\n")

# ⚠️ 关键：E5 必须加前缀！
query = "query: 如何配置 Docker 网络"
passages = [
    "passage: Docker network 配置命令：docker network create --driver bridge",
    "passage: 今天天气很好，适合出门散步",
    "passage: Docker container networking best practices for production",
    "passage: Python 列表推导式语法：[x*2 for x in range(10)]",
    "passage: Linux 权限管理：chmod 755 file.txt"
]

# 生成向量
query_emb = model.encode(query, normalize_embeddings=True)
passage_embs = model.encode(passages, normalize_embeddings=True)

# 计算相似度
scores = cos_sim(query_emb, passage_embs)[0]

# 排序输出
results = sorted(zip(passages, scores), key=lambda x: x[1], reverse=True)

print(f"查询：{query.replace('query: ', '')}\n")
print(f"{'排名':<4} {'相似度':<8} {'内容'}")
print("-" * 60)
for i, (passage, score) in enumerate(results, 1):
    print(f"{i:<4} {score:.4f}   {passage.replace('passage: ', '')}")
