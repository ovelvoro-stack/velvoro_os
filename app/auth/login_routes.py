from fastapi import APIRouter
from app.auth.auth_utils import create_access_token

router = APIRouter()

@router.post("/login")
def login(username: str, role: str = "user"):
    token = create_access_token({"sub": username, "role": role})
    return {"access_token": token, "token_type": "bearer"}
