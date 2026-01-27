from fastapi import APIRouter, Depends
from app.core.security import get_current_user
from app.services.summary_service import daily_summary

router = APIRouter()

@router.get("/")
def summary(user=Depends(get_current_user)):
    return daily_summary(user)
