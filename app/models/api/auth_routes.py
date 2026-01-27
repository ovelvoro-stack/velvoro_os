from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(data: LoginRequest):
    if data.username == "admin" and data.password == "admin":
        return {
            "status": "success",
            "user": "admin",
            "role": "admin"
        }
    raise HTTPException(status_code=401, detail="Invalid credentials")
