from fastapi import APIRouter
from app.services.summary_service import daily_summary

router = APIRouter(prefix="/summary")

@router.get("/daily")
def summary():
    return daily_summary()
