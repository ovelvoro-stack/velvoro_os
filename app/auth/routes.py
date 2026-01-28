from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.core.security import verify_password, create_access_token
from app.db.excel_db import get_user_by_credentials

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user_by_credentials(
        username=form_data.username,
        password=form_data.password,
    )

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(
        data={
            "username": user["username"],
            "role": user["role"],
            "company_name": user["company_name"],
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }
