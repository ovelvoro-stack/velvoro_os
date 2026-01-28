from fastapi import APIRouter
from app.services.task_service import create_task
from app.services.followup_service import create_followup

router = APIRouter(prefix="/employee")

@router.post("/task")
def add_task(data: dict):
    create_task(data["user"], data["task"])
    return {"status": "task saved"}

@router.post("/followup")
def add_followup(data: dict):
    create_followup(data["user"], data["note"], data["due_date"])
    return {"status": "followup saved"}
