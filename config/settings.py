# config/settings.py
import os

VIBE_SCRIPT_PATH = os.environ.get("VIBE_SCRIPT_PATH", "VIBE/demo.py")
MOTIONBERT_CHECKPOINT = os.environ.get("MOTIONBERT_CHECKPOINT", "MotionBERT/checkpoint/pretrain/MB_release/latest_epoch.bin")
MOTIONBERT_CONFIG = os.environ.get("MOTIONBERT_CONFIG", "MotionBERT/configs/pretrain/MB_pretrain.yaml")
DB_PATH = os.environ.get("DB_PATH", "rhythm_heritage.db")
