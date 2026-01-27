import os

DATA_DIR = "data"
JWT_SECRET = os.getenv("JWT_SECRET", "velvoro-secret")
AI_MODE = os.getenv("AI_MODE", "stub")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
