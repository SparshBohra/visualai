# main.py
import os
import sys

from config.settings import VIBE_SCRIPT_PATH, MOTIONBERT_CHECKPOINT, MOTIONBERT_CONFIG

from services.embedding_service import EmbeddingService
from services.storage_service import SQLiteStorageService

def main():
    video_path = "test.mp4"  # Update if you want a CLI arg

    if not os.path.exists(video_path):
        print(f"❌ Video file not found: {video_path}")
        sys.exit(1)

    # Paths to VIBE & MotionBERT
    vibe_script_path = "VIBE/demo.py"
    motionbert_checkpoint = "MotionBERT/checkpoint/pretrain/MB_release/latest_epoch.bin"
    motionbert_config = "MotionBERT/configs/pretrain/MB_pretrain.yaml"

    # Initialize pipeline
    embedder = EmbeddingService(
        vibe_script_path=vibe_script_path,
        motionbert_checkpoint=motionbert_checkpoint,
        motionbert_config=motionbert_config
    )
    storage = SQLiteStorageService()  # Will create rhythm_heritage.db

    # Process video → generate embedding
    print("⚙️ Processing video...")
    embedding = embedder.process_video(video_path)

    # Example user + dance name
    user_id = "elder_001"
    dance_name = "SampleDance"

    # Save embedding in DB
    storage.save_embedding(user_id, dance_name, embedding)
    print("✅ All done! Check 'rhythm_heritage.db' for stored embeddings.")

if __name__ == "__main__":
    main()
