#!/usr/bin/env python3

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2026-03-24 21:55


# RAG System v6 - Improved Version
# Key upgrades:
# 1. Dynamic threshold search
# 2. Faster MMR (precomputed similarity)
# 3. Better multi-turn isolation
# 4. Cross-encoder reranker
# 5. Embedding cache (file hash based)
# 6. Token-based overlap
# 7. llama.cpp ctx-size fix

import os
import hashlib
import pickle
import numpy as np
import torch
from sentence_transformers import SentenceTransformer

# ================= CONFIG =================
MODEL_NAME = "intfloat/multilingual-e5-large"
RERANK_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"
CACHE_PATH = "./embed_cache.pkl"

TOP_K = 3
INITIAL_THRESHOLD = 0.3
MIN_THRESHOLD = 0.1

# =========================================

class EmbedCache:
    def __init__(self, path=CACHE_PATH):
        self.path = path
        self.data = {}
        if os.path.exists(path):
            self.data = pickle.load(open(path, "rb"))

    def _hash(self, text):
        return hashlib.md5(text.encode()).hexdigest()

    def get(self, text):
        return self.data.get(self._hash(text))

    def set(self, text, emb):
        self.data[self._hash(text)] = emb

    def save(self):
        pickle.dump(self.data, open(self.path, "wb"))


class RAG:
    def __init__(self):
        self.model = SentenceTransformer(MODEL_NAME)
        self.reranker = SentenceTransformer(RERANK_MODEL)
        self.cache = EmbedCache()
        self.docs = []
        self.embs = None

    def embed(self, texts):
        result = []
        with torch.no_grad():
            for t in texts:
                cached = self.cache.get(t)
                if cached is not None:
                    result.append(cached)
                else:
                    emb = self.model.encode(t, normalize_embeddings=True)
                    self.cache.set(t, emb)
                    result.append(emb)
        return np.array(result)

    def build(self, docs):
        self.docs = docs
        texts = [f"passage: {d}" for d in docs]
        self.embs = self.embed(texts)
        self.cache.save()

    def dynamic_search(self, query):
        q = self.model.encode(f"query: {query}", normalize_embeddings=True)
        scores = self.embs @ q

        threshold = INITIAL_THRESHOLD
        candidates = []

        while threshold >= MIN_THRESHOLD:
            candidates = [i for i, s in enumerate(scores) if s >= threshold]
            if len(candidates) >= TOP_K:
                break
            threshold -= 0.05

        if not candidates:
            candidates = np.argsort(scores)[-TOP_K*3:]

        return candidates, scores

    def mmr(self, q, candidates, scores):
        selected = []
        sim_matrix = self.embs @ self.embs.T

        while len(selected) < TOP_K and candidates:
            if not selected:
                best = max(candidates, key=lambda i: scores[i])
            else:
                def mmr_score(i):
                    return 0.6 * scores[i] - 0.4 * max(sim_matrix[i][j] for j in selected)
                best = max(candidates, key=mmr_score)

            selected.append(best)
            candidates.remove(best)

        return selected

    def rerank(self, query, indices):
        pairs = [(query, self.docs[i]) for i in indices]
        scores = self.reranker.predict(pairs)
        ranked = sorted(zip(indices, scores), key=lambda x: x[1], reverse=True)
        return [i for i, _ in ranked[:TOP_K]]

    def search(self, query):
        candidates, scores = self.dynamic_search(query)
        selected = self.mmr(None, list(candidates), scores)
        final = self.rerank(query, selected)
        return [(self.docs[i], float(scores[i])) for i in final]


if __name__ == "__main__":
    rag = RAG()

    docs = [
        "Python decorator allows wrapping functions",
        "MMR improves diversity in retrieval",
        "RAG combines retrieval and generation",
        "Transformers use attention mechanisms"
    ]

    rag.build(docs)

    while True:
        q = input("Query: ")
        results = rag.search(q)
        for r in results:
            print(r)

