from fastapi import APIRouter
from app.services.task_service import list_tasks
from app.services.followup_service import list_followups

router = APIRouter(prefix="/manager")

@router.get("/tasks")
def tasks():
    return list_tasks()

@router.get("/followups")
def followups():
    return list_followups()
