from fastapi import APIRouter
from app.models.services.task_service import list_tasks

router = APIRouter()

@router.get("/daily-summary/")
def daily_summary():
    return list_tasks()
