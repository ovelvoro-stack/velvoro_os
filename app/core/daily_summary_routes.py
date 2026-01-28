from fastapi import APIRouter

router = APIRouter()

@router.get("/daily-summary")
def daily_summary():
    return {
        "status": "ok",
        "message": "Daily summary endpoint active"
    }
