from fastapi import APIRouter
from app.models.services.task_service import add_task

router = APIRouter()

@router.post("/api/employee/task")
def employee_task(data: dict):
    add_task(data["user"], data["task"])
    return {"status": "saved"}
