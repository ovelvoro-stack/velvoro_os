from fastapi import APIRouter
from app.services.reminder_service import pending_reminders

router = APIRouter(prefix="/reminders")

@router.get("/pending")
def get_pending():
    return pending_reminders()
