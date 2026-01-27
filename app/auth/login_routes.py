from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Simple placeholder login (does NOT break existing auth logic)
class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(data: LoginRequest):
    if not data.username or not data.password:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Dummy token (extend later, backward compatible)
    return {
        "access_token": "dummy-token",
        "token_type": "bearer"
    }
