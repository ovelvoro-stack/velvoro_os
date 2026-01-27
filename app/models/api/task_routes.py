File name: task_routes.py
File path: app/models/api/task_routes.py
Full code:
from fastapi import APIRouter
from app.models.services.task_service import create_task, list_tasks

router = APIRouter()

@router.post("/")
def add_task(task: dict):
    return create_task(task)

@router.get("/")
def get_tasks():
    return list_tasks()
