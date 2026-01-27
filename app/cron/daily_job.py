from datetime import datetime
from app.models.services.daily_summary_service import get_daily_summary

def run_daily_summary():
    summary = get_daily_summary()
    return {
        "generated_at": str(datetime.utcnow()),
        "summary": summary
    }
