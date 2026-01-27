from fastapi import APIRouter
from app.services.daily_summary_service import build_daily_summary

router = APIRouter()

@router.get("/daily-summary")
def daily_summary():
    return build_daily_summary()
