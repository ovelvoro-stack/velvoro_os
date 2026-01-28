from fastapi import APIRouter
from app.services.task_service import list_tasks

router = APIRouter()

@router.get("/api/manager/tasks")
def get_tasks():
    return list_tasks()
