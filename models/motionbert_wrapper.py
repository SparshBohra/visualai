# models/motionbert_wrapper.py

import torch
import numpy as np

class MotionBERTWrapper:
    """
    A minimal wrapper for your MotionBERT model.
    Expects a checkpoint file 'latest_epoch.bin' and a config YAML.
    """

    def __init__(self, checkpoint="latest_epoch.bin", config="pretrain/MB_pretrain.yaml"):
        # Pseudocode for loading your MotionBERT model
        # Real code depends on the official implementation's structure

        # Example:
        # self.model = YourMotionBERTClass(config)
        # checkpoint_data = torch.load(checkpoint, map_location="cpu")
        # self.model.load_state_dict(checkpoint_data['model'])
        # self.model.eval()

        self.model = None  # Replace with actual loaded model
        self.config = config
        self.checkpoint = checkpoint
        print(f"[MotionBERTWrapper] Initialized with {checkpoint} and {config}")

    def encode(self, joints3D: np.ndarray) -> np.ndarray:
        """
        Takes an array of shape (T, 24, 3) representing 3D joints over time
        and returns a single embedding vector, e.g. shape (512,).
        """
        if self.model is None:
            # This is where you'd run a forward pass on the actual model
            # For now, let's just mock a random embedding
            T = joints3D.shape[0]
            # Suppose final embedding is 512D
            embedding = np.random.rand(512).astype(np.float32)
            return embedding

        # Real code example:
        # input_tensor = torch.from_numpy(joints3D).unsqueeze(0)  # (1, T, 24, 3)
        # embedding = self.model(input_tensor)  # shape (1, 512)
        # return embedding.squeeze(0).cpu().numpy()

        # (Pseudo fallback)
        return np.random.rand(512).astype(np.float32)
