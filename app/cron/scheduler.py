from apscheduler.schedulers.background import BackgroundScheduler
from app.models.services.daily_summary_service import generate_daily_summary

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(generate_daily_summary, "cron", hour=21, minute=0)
    scheduler.start()
