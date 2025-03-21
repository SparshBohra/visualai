# services/similarity_service.py

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from services.storage_service import SQLiteStorageService

class SimilarityService:
    def __init__(self):
        self.db = SQLiteStorageService()

    def find_most_similar_dance(self, user_embedding: np.ndarray):
        """
        Compare user_embedding with all stored embeddings in DB
        Return (best_match_dance_name, best_score)
        """
        all_entries = self.db.get_all_embeddings()
        # all_entries is a list of tuples: (user_id, dance_name, embedding_str)

        best_score = -1.0
        best_dance = None

        user_emb = user_embedding.reshape(1, -1)

        for (user_id, dance_name, emb_str) in all_entries:
            float_list = list(map(float, emb_str.split(',')))
            db_emb = np.array(float_list).reshape(1, -1)

            score = cosine_similarity(user_emb, db_emb)[0][0]
            if score > best_score:
                best_score = score
                best_dance = dance_name

        return best_dance, best_score
