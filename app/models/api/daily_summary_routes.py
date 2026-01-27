from fastapi import APIRouter
from datetime import date
from typing import List, Dict, Any

router = APIRouter(
    prefix="/daily-summary",
    tags=["Daily Summary"]
)


@router.get("/", response_model=Dict[str, Any])
def get_daily_summary():
    """
    Daily Summary Engine
    - Tasks
    - Pending follow-ups
    - AI suggestion (stub)
    """

    summary_data = {
        "date": str(date.today()),
        "tasks": [
            {
                "id": 1,
                "title": "Review pending tasks",
                "status": "pending",
                "priority": "high"
            },
            {
                "id": 2,
                "title": "Send follow-up emails",
                "status": "completed",
                "priority": "medium"
            }
        ],
        "pending_followups": [
            {
                "id": 101,
                "note": "Call client regarding proposal",
                "due_time": "16:00"
            }
        ],
        "ai_suggestion": "Focus on completing one high-impact task before noon."
    }

    return summary_data
