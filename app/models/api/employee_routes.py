from fastapi import APIRouter, Body
from app.services.task_service import add_task

router = APIRouter()

@router.post("/api/employee/task")
def create_task(payload: dict = Body(...)):
    user = payload.get("user")
    task = payload.get("task")
    add_task(user, task)
    return {"status": "saved"}
