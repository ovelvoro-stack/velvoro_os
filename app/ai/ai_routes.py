from fastapi import APIRouter, HTTPException
from app.ai.usage_service import track, allowed

router = APIRouter(prefix="/ai", tags=["ai"])

@router.post("/use/{company}")
def use_ai(company: str, tokens: int = 100):
    if not allowed(company, tokens):
        raise HTTPException(status_code=403, detail="AI limit exceeded")
    track(company, tokens)
    return {"status": "ok", "tokens_used": tokens}
