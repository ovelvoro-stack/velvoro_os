from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.models.auth.jwt_utils import create_access_token

router = APIRouter()

# EXISTING SIMPLE LOGIN → now JWT-enabled (still backward compatible)
class LoginRequest(BaseModel):
    username: str
    password: str


@router.post("/login")
def login(data: LoginRequest):
    if data.username == "admin" and data.password == "admin":
        token = create_access_token(
            {
                "sub": data.username,
                "role": "admin",
            }
        )
        return {
            "status": "success",
            "user": "admin",
            "role": "admin",
            "access_token": token,
            "token_type": "bearer",
        }

    if data.username == "user" and data.password == "user":
        token = create_access_token(
            {
                "sub": data.username,
                "role": "user",
            }
        )
        return {
            "status": "success",
            "user": "user",
            "role": "user",
            "access_token": token,
            "token_type": "bearer",
        }

    raise HTTPException(status_code=401, detail="Invalid credentials")
