from fastapi import APIRouter
from app.models.services.task_service import list_tasks, approve_task

router = APIRouter()

@router.get("/api/manager/tasks/{company_id}")
def get_tasks(company_id: str):
    return list_tasks(company_id)

@router.post("/api/manager/approve/{task_id}")
def approve(task_id: str):
    approve_task(task_id)
    return {"status": "approved"}
