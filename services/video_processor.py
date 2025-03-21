# services/video_processor.py
import cv2
import os

class VideoProcessor:
    def __init__(self, out_fps=30, out_width=640, out_height=480):
        self.out_fps = out_fps
        self.out_width = out_width
        self.out_height = out_height

    def preprocess_video(self, in_path: str, out_path: str):
        if not os.path.exists(in_path):
            raise FileNotFoundError(f"Video not found: {in_path}")

        cap = cv2.VideoCapture(in_path)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(out_path, fourcc, self.out_fps, (self.out_width, self.out_height))

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            resized = cv2.resize(frame, (self.out_width, self.out_height))
            out.write(resized)

        cap.release()
        out.release()
        return out_path
