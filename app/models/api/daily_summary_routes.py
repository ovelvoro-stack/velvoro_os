from fastapi import APIRouter
from app.models.services.daily_summary_service import get_daily_summary

router = APIRouter()

@router.get("/")
def daily_summary():
    return get_daily_summary()
