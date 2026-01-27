from fastapi import APIRouter
from app.services.daily_summary_service import (
    add_task,
    add_followup,
    get_daily_summary
)

router = APIRouter()

@router.get("/summary")
def daily_summary():
    return get_daily_summary()

@router.post("/task")
def create_task(title: str):
    return add_task(title)

@router.post("/followup")
def create_followup(note: str, due_date: str):
    return add_followup(note, due_date)
