from datetime import date
import uuid
from app.database import read_sheet, write_sheet

# ---------------- TASKS ----------------
def add_task(title: str):
    df = read_sheet("tasks")
    row = {
        "id": str(uuid.uuid4()),
        "title": title,
        "status": "pending",
        "created": str(date.today())
    }
    df = df._append(row, ignore_index=True)
    write_sheet("tasks", df)
    return row

# ---------------- FOLLOWUPS ----------------
def add_followup(note: str, due_date: str):
    df = read_sheet("followups")
    row = {
        "id": str(uuid.uuid4()),
        "note": note,
        "due_date": due_date
    }
    df = df._append(row, ignore_index=True)
    write_sheet("followups", df)
    return row

# ---------------- AI SUGGESTION (STUB) ----------------
def ai_suggestion(tasks_count: int):
    if tasks_count == 0:
        return "Start with one important task today."
    if tasks_count > 5:
        return "Too many tasks. Focus on top 1–2 only."
    return "Good pace. Finish pending tasks."

# ---------------- DAILY SUMMARY ----------------
def get_daily_summary():
    tasks = read_sheet("tasks")
    followups = read_sheet("followups")

    return {
        "date": str(date.today()),
        "tasks": tasks.to_dict(orient="records"),
        "followups": followups.to_dict(orient="records"),
        "ai_suggestion": ai_suggestion(len(tasks))
    }
