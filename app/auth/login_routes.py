from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(data: LoginRequest):
    # minimal stub auth (existing features untouched)
    if not data.username or not data.password:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {
        "access_token": "dummy-token",
        "token_type": "bearer"
    }
