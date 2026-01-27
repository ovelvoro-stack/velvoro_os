from datetime import date
import uuid
from app.database import read_sheet, write_sheet

def get_daily_summary():
    tasks_df = read_sheet("tasks")
    followups_df = read_sheet("followups")

    return {
        "date": str(date.today()),
        "tasks": tasks_df.to_dict(orient="records"),
        "followups": followups_df.to_dict(orient="records"),
        "ai_suggestion": generate_ai_suggestion(tasks_df)
    }

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

def generate_ai_suggestion(tasks_df):
    if len(tasks_df) == 0:
        return "Plan one high-impact task today"
    pending = tasks_df[tasks_df["status"] == "pending"]
    if len(pending) > 3:
        return "Reduce task load and focus on 1–2 priorities"
    return "Focus on completing pending tasks"
