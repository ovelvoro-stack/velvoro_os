from fastapi import APIRouter
from app.db.excel_db import load_excel, save_excel

manager_router = APIRouter(prefix="/manager", tags=["manager"])

@manager_router.get("/pending-tasks")
def pending_tasks(company_name: str):
    tasks = load_excel("tasks.xlsx")
    return tasks[
        (tasks.company_name == company_name) &
        (tasks.status == "pending")
    ].to_dict(orient="records")

@manager_router.post("/approve")
def approve_task(task_id: int):
    tasks = load_excel("tasks.xlsx")
    tasks.loc[tasks.id == task_id, "status"] = "approved"
    save_excel("tasks.xlsx", tasks)
    return {"status": "approved"}
