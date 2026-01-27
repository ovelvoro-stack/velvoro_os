from fastapi import APIRouter
from app.auth.jwt_auth import create_token

router = APIRouter()

@router.post("/login")
def login(username: str, password: str):
    # demo auth (replace later)
    if username == "admin" and password == "admin":
        token = create_token({"sub": username})
        return {"access_token": token, "token_type": "bearer"}
    return {"error": "Invalid credentials"}
