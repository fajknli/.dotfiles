#!/usr/bin/env python3

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2026-03-25 17:18


import numpy as np

def mmr_rerank(
        query_emb: np.ndarray,
        candidate_embs: np.ndarray,
        candidate_indices: list[int],
        top_k: int,
        lambda_param: float = 0.7,
) -> list[int]:
    if len(candidate_indices) <= top_k:
        return candidate_indices

    query_emb = np.array(query_emb)
    selected = []
    remaining = list(candidate_indices)

    # 计算query相似度
    rel_scores = {}
    for idx in remaining:
        sim = float(np.dot(query_emb, candidate_embs[idx]))
        rel_scores[idx] = sim

    print("与query的相似度为")
    for k, v in rel_scores.items():
        print(f"idx={k}, score={v:.3f}")

    print("\n开始选择: \n")

    # 逐个选择
    while len(selected) < top_k and remaining:
        if not selected:
            best = max(remaining, key=lambda i: rel_scores[i])
            print(f"第一轮:选择 idx={best} (最相关)")
        else:
            sel_embs = candidate_embs[selected]
            best, best_score = None, -np.inf

            for idx in remaining:
                emb = candidate_embs[idx]

                # 和已选集合的最大相似度
                max_sim = float(np.max(sel_embs @ emb))

                mmr_score = (lambda_param * rel_scores[idx] - (1 -lambda_param) * max_sim)

                print(
                        f"候选 idx={idx} | rel={rel_scores[idx]:.3f},"
                        f"dup={max_sim:.3f}, mmr={mmr_score:.3f}"
                        )
                if mmr_score > best_score:
                    best_score = mmr_score
                    best = idx

            print(f"选择 idx={best}\n")

        selected.append(best)
        remaining.remove(best)

    return selected

# =========================
# 🎯 构造一个简单例子
# =========================

# query（比如：想找“机器学习”）
query = np.array([1.0, 0.0])

# 候选向量（人为设计，让你看得懂）
candidate_embs = np.array([
    [0.9, 0.1],   # 0：很像 query（机器学习基础）
    [0.85, 0.15], # 1：也很像（重复内容）
    [0.1, 0.9],   # 2：完全不同（比如：艺术）
    [0.6, 0.4],   # 3：中等相关（数据分析）
    [0.0, 1.0],   # 4：完全无关
])

candidate_indices = [0, 1, 2, 3, 4]

# =========================
# 🚀 跑 MMR
# =========================

result = mmr_rerank(
    query_emb=query,
    candidate_embs=candidate_embs,
    candidate_indices=candidate_indices,
    top_k=3,
    lambda_param=0.7,
)

print("最终选择：", result)
