from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.security import (
    verify_password,
    create_access_token,
    create_refresh_token,
    decode_token,
)
from app.db.users import get_user_by_credentials

auth_router = APIRouter(prefix="/auth")


class LoginRequest(BaseModel):
    company_name: str
    username: str
    password: str


@auth_router.post("/login")
def login(data: LoginRequest):
    user = get_user_by_credentials(
        data.company_name, data.username
    )

    if not user or not verify_password(data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    payload = {
        "company": user["company_name"],
        "username": user["username"],
        "role": user["role"],
    }

    return {
        "access_token": create_access_token(payload),
        "refresh_token": create_refresh_token(payload),
    }


@auth_router.post("/refresh")
def refresh_token(token: str):
    payload = decode_token(token)
    if payload.get("type") != "refresh":
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    new_payload = {
        "company": payload["company"],
        "username": payload["username"],
        "role": payload["role"],
    }

    return {
        "access_token": create_access_token(new_payload)
    }
