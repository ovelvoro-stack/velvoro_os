from fastapi import APIRouter
from app.services.daily_summary_service import (
    get_daily_summary,
    add_task,
    add_followup
)
from app.models.schemas import TaskCreate, FollowupCreate

router = APIRouter()

@router.get("/")
def daily_summary():
    return get_daily_summary()

@router.post("/task")
def create_task(payload: TaskCreate):
    add_task(payload.title)
    return {"message": "Task added"}

@router.post("/followup")
def create_followup(payload: FollowupCreate):
    add_followup(payload.note, payload.due_date)
    return {"message": "Follow-up added"}
