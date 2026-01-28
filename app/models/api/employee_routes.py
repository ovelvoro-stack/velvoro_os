from fastapi import APIRouter, Request
from pydantic import BaseModel
from app.models.services.task_service import add_task
from app.core.auth_middleware import require_role

router = APIRouter()

class TaskRequest(BaseModel):
    company_id: str
    employee: str
    task: str

@router.post("/api/employee/task")
async def create_task(data: TaskRequest, request: Request):
    await require_role(request, ["employee"])
    add_task(data.company_id, data.employee, data.task)
    return {"status": "saved"}
