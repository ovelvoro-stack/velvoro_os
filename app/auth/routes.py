from fastapi import APIRouter, HTTPException
from app.db.excel_db import get_user_by_credentials

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/login")
def login(payload: dict):
    username = payload.get("username")
    password = payload.get("password")

    user = get_user_by_credentials(username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "status": "success",
        "user": user
    }
