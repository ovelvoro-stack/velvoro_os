from datetime import date
from app.database import read_sheet, write_sheet
import uuid

def add_task(title: str):
    df = read_sheet("tasks")
    df.loc[len(df)] = {
        "id": str(uuid.uuid4()),
        "title": title,
        "status": "pending"
    }
    write_sheet("tasks", df)

def add_followup(note: str, due_date: str):
    df = read_sheet("followups")
    df.loc[len(df)] = {
        "id": str(uuid.uuid4()),
        "note": note,
        "due_date": due_date
    }
    write_sheet("followups", df)

def get_daily_summary():
    tasks_df = read_sheet("tasks")
    followups_df = read_sheet("followups")

    return {
        "date": str(date.today()),
        "tasks": tasks_df.to_dict(orient="records"),
        "pending_followups": followups_df.to_dict(orient="records"),
        "ai_suggestion": "Complete pending tasks before adding new ones."
    }
