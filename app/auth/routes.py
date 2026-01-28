from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from app.db.excel_db import get_user_by_credentials

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/login")
def login_get():
    return JSONResponse(
        status_code=200,
        content={"message": "Login endpoint is alive. Use POST to authenticate."}
    )

@auth_router.post("/login")
def login_post(username: str, password: str):
    user = get_user_by_credentials(username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    return user
