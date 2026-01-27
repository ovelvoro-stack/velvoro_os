from app.models.services.daily_summary_service import get_daily_summary

def run_daily_job():
    return get_daily_summary()
