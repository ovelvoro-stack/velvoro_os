from fastapi import APIRouter
from app.db.excel_db import load_excel

employee_router = APIRouter(prefix="/employee", tags=["employee"])

@employee_router.get("/summary")
def summary(company_name: str, username: str):
    tasks = load_excel("tasks.xlsx")
    return tasks[
        (tasks.company_name == company_name) &
        (tasks.username == username)
    ].to_dict(orient="records")
