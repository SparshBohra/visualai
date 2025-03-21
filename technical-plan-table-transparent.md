# Dance Heritage Platform: Technical Implementation Plan

| Step | Task | Tools |
|:---:|:---|:---|
| 1️⃣ | **Elder Uploads a Dance** <br>Elders submit videos + metadata | Django/Flask + S3 |
| 2️⃣ | **Process Video (3D Data)** <br>Extract motion joints | VIBE |
| 3️⃣ | **Generate Embeddings** <br>Convert motion to fixed-size vectors | MotionBERT |
| 4️⃣ | **Fine-Tune** <br>Train a dance classifier | MotionBERT / Transformer |
| 5️⃣ | **User Selects Dance** <br>Chooses from library | Frontend UI + API |
| 6️⃣ | **User Practices** <br>Records dance attempt | Frontend Camera |
| 7️⃣ | **Process User Dance** <br>Again: VIBE + MotionBERT | ML Inference |
| 8️⃣ | **Compare & Score** <br>Cosine similarity vs. elder dance | Cosine API |
| 9️⃣ | **Feedback & Recommendations** <br>Suggest similar dances | Fine-Tuned Model API |
