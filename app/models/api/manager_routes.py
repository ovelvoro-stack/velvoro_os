from fastapi import APIRouter
from app.models.services.task_service import list_tasks

router = APIRouter()

@router.get("/api/manager/tasks")
def manager_tasks():
    return list_tasks()
