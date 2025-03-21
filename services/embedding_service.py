# services/embedding_service.py

import numpy as np
from models.vibe_wrapper import VIBEWrapper
from models.motionbert_wrapper import MotionBERTWrapper

class EmbeddingService:
    def __init__(self, vibe_script_path: str, motionbert_checkpoint: str, motionbert_config: str):
        self.vibe_wrapper = VIBEWrapper(vibe_script_path)
        self.motionbert_wrapper = MotionBERTWrapper(
            checkpoint=motionbert_checkpoint,
            config=motionbert_config
        )

    def process_video(self, video_path: str) -> np.ndarray:
        """
        1. Run VIBE to get 3D joints
        2. Run MotionBERT to get an embedding
        """
        vibe_output = self.vibe_wrapper.run(video_path)
        joints3D = vibe_output["joints3D"]  # shape [T, 24, 3]
        embedding = self.motionbert_wrapper.encode(joints3D)
        return embedding
