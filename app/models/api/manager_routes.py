from fastapi import APIRouter, Request
from app.models.services.task_service import list_tasks, approve_task
from app.core.auth_middleware import require_role

router = APIRouter()

@router.get("/api/manager/tasks/{company_id}")
async def get_tasks(company_id: str, request: Request):
    await require_role(request, ["manager"])
    return list_tasks(company_id)

@router.post("/api/manager/approve/{task_id}")
async def approve(task_id: str, request: Request):
    await require_role(request, ["manager"])
    approve_task(task_id)
    return {"status": "approved"}
