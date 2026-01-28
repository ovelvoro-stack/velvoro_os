from fastapi import APIRouter, HTTPException
from app.db.excel_db import load_excel
from app.core.security import verify_password

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/login")
def login(company_name: str, username: str, password: str):
    users = load_excel("users.xlsx")

    user = users[
        (users.company_name == company_name) &
        (users.username == username)
    ]

    if user.empty:
        raise HTTPException(401, "Invalid credentials")

    row = user.iloc[0]

    if row.active_status != "active":
        raise HTTPException(403, "User disabled")

    if row.plan_status != "active":
        raise HTTPException(402, "Company plan expired")

    if not verify_password(password, row.password):
        raise HTTPException(401, "Invalid credentials")

    return {
        "company": company_name,
        "username": username,
        "role": row.role
    }
