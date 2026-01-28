from fastapi import APIRouter
from app.db.excel_db import load_excel, save_excel
from app.core.security import hash_password

admin_router = APIRouter(prefix="/admin", tags=["admin"])

@admin_router.post("/create-user")
def create_user(
    company_name: str,
    username: str,
    password: str,
    role: str
):
    users = load_excel("users.xlsx")

    users.loc[len(users)] = {
        "company_name": company_name,
        "username": username,
        "password": hash_password(password),
        "role": role,
        "active_status": "active",
        "plan_status": "active"
    }

    save_excel("users.xlsx", users)
    return {"created": username}
