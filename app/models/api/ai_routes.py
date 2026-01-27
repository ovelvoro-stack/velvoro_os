from fastapi import APIRouter
from app.llm.llm_client import generate_ai_text

router = APIRouter()

@router.post("/ai/suggest")
def ai_suggest(prompt: str):
    return {"suggestion": generate_ai_text(prompt)}
