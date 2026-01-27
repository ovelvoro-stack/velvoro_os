from datetime import date
from app.services.task_service import list_tasks
from app.services.followup_service import list_followups
from app.core.ai_engine import generate_ai_suggestion

def daily_summary(user):
    tasks = list_tasks(user)
    followups = list_followups(user)
    return {
        "date": str(date.today()),
        "tasks": tasks,
        "followups": followups,
        "ai_suggestion": generate_ai_suggestion(tasks, followups)
    }
