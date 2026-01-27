from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Login(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(data: Login):
    if data.username == "admin" and data.password == "admin":
        return {"user": "admin", "role": "admin", "api_key": "admin"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
