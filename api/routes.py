# api/routes.py
from flask import request, jsonify
from . import create_app
from services.embedding_service import EmbeddingService
from services.storage_service import SQLiteStorageService

app = create_app()

@app.route('/upload', methods=['POST'])
def upload_video():
    # handle file upload, call embedding service, store in DB
    return jsonify({"status": "ok"})

# Additional routes as needed
