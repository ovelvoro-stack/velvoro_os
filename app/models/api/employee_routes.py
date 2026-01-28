from fastapi import APIRouter
from pydantic import BaseModel
from app.models.services.task_service import add_task

router = APIRouter()

class TaskRequest(BaseModel):
    company_id: str
    employee: str
    task: str

@router.post("/api/employee/task")
def create_task(data: TaskRequest):
    add_task(data.company_id, data.employee, data.task)
    return {"status": "saved"}
