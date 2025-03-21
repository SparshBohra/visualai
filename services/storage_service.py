# services/storage_service.py

import sqlite3
import numpy as np
import os

class SQLiteStorageService:
    def __init__(self, db_path="rhythm_heritage.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self._create_table()

    def _create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS motion_embeddings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                dance_name TEXT NOT NULL,
                embedding TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def save_embedding(self, user_id: str, dance_name: str, embedding: np.ndarray):
        embedding_str = ','.join(map(str, embedding.tolist()))
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO motion_embeddings (user_id, dance_name, embedding)
            VALUES (?, ?, ?)
        ''', (user_id, dance_name, embedding_str))
        self.conn.commit()
        print(f"[SQLite] Saved embedding for user={user_id}, dance={dance_name}")

    def get_all_embeddings(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT user_id, dance_name, embedding FROM motion_embeddings")
        results = cursor.fetchall()
        return results
