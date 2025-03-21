# models/vibe_wrapper.py
import subprocess
import os
import pickle
import numpy as np

class VIBEWrapper:
    """
    A real wrapper to run VIBE from local VIBE/demo.py and parse .pkl output.
    """

    def __init__(self, vibe_script_path="VIBE/demo.py", output_dir="data/vibe_output"):
        self.vibe_script = vibe_script_path
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def run(self, video_path: str):
        print(f"[VIBE] Running on: {video_path}")
        video_name = os.path.basename(video_path).split('.')[0]
        output_path = os.path.join(self.output_dir, f"{video_name}.pkl")

        if os.path.exists(output_path):
            print(f"[VIBE] Using cached output at: {output_path}")
        else:
            cmd = [
                "python",
                self.vibe_script,
                "--vid_file", video_path,
                "--output_folder", self.output_dir,
                "--no_render"
            ]
            subprocess.run(cmd, check=True)
            print(f"[VIBE] Saved output to: {output_path}")

        # Load and parse the .pkl file
        if not os.path.exists(output_path):
            raise FileNotFoundError(f"[VIBE] Output not found: {output_path}")

        with open(output_path, "rb") as f:
            vibe_output = pickle.load(f)

        # Use first key (usually video name)
        key = list(vibe_output.keys())[0]
        frames = vibe_output[key]

        joints3D = np.array([frame['joints3d'] for frame in frames], dtype=np.float32)

        return {
            "joints3D": joints3D,
            "pose": None,
            "trans": None
        }
