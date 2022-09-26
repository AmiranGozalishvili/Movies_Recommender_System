import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def cosine_similarity_ranking(query, items, top_k=5):
    similarities = cosine_similarity(np.array([query]), np.array(items.tolist()))

    topk_indices = np.argsort((similarities.reshape(-1)))[::-1][:top_k]

    return topk_indices
