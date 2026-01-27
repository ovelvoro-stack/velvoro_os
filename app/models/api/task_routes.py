from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.core.security import get_current_user
from app.services.task_service import create_task, list_tasks

router = APIRouter()

class TaskReq(BaseModel):
    title: str
    priority: str = "normal"

@router.post("/")
def add_task(data: TaskReq, user=Depends(get_current_user)):
    return create_task(data.title, data.priority, user)

@router.get("/")
def get_tasks(user=Depends(get_current_user)):
    return list_tasks(user)
