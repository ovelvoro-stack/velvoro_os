from fastapi import APIRouter, HTTPException
from app.services.auth_service import authenticate_user

router = APIRouter(prefix="/auth")

@router.post("/login")
def login(data: dict):
    user = authenticate_user(
        username=data.get("username"),
        password=data.get("password")
    )

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "status": "success",
        "user_id": user["user_id"],
        "name": user["name"],
        "role": user["role"]
    }
