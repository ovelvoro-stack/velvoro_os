from datetime import date
from app.models.task_model import fetch_today_tasks

def build_daily_summary():
    tasks = fetch_today_tasks()

    completed = [t for t in tasks if t["status"] == "done"]
    pending = [t for t in tasks if t["status"] != "done"]

    ai_suggestion = (
        "Focus on completing one high-impact pending task today."
        if pending else
        "Great job! All tasks are completed. Plan tomorrow early."
    )

    return {
        "date": str(date.today()),
        "total_tasks": len(tasks),
        "completed_tasks": len(completed),
        "pending_tasks": pending,
        "ai_suggestion": ai_suggestion
    }
