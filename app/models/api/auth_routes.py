from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.models.services.auth_service import authenticate

router = APIRouter()

class LoginRequest(BaseModel):
    company_id: str
    username: str
    password: str

@router.post("/auth/login")
def login(data: LoginRequest):
    user = authenticate(data.company_id, data.username, data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"status": "ok", "user": user}
