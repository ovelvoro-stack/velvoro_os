import pandas as pd
from datetime import datetime
import os

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

TASKS_FILE = f"{DATA_DIR}/tasks.xlsx"
FOLLOWUPS_FILE = f"{DATA_DIR}/followups.xlsx"
SUMMARY_FILE = f"{DATA_DIR}/daily_summary.xlsx"

def _load(file, columns):
    if os.path.exists(file):
        return pd.read_excel(file)
    return pd.DataFrame(columns=columns)

def _save(df, file):
    df.to_excel(file, index=False)

def add_task(user, task):
    df = _load(TASKS_FILE, ["user", "task", "date", "status"])
    df.loc[len(df)] = [user, task, datetime.now().date(), "pending"]
    _save(df, TASKS_FILE)

def add_followup(user, note, due_date):
    df = _load(FOLLOWUPS_FILE, ["user", "note", "due_date", "status"])
    df.loc[len(df)] = [user, note, due_date, "pending"]
    _save(df, FOLLOWUPS_FILE)

def get_tasks():
    return _load(TASKS_FILE, []).to_dict(orient="records")

def get_followups():
    return _load(FOLLOWUPS_FILE, []).to_dict(orient="records")

def generate_summary():
    tasks = _load(TASKS_FILE, [])
    followups = _load(FOLLOWUPS_FILE, [])
    today = datetime.now().date()

    summary = {
        "date": today,
        "tasks_total": len(tasks),
        "tasks_pending": len(tasks[tasks["status"] == "pending"]),
        "followups_pending": len(followups[followups["status"] == "pending"])
    }

    df = _load(SUMMARY_FILE, ["date", "tasks_total", "tasks_pending", "followups_pending"])
    df.loc[len(df)] = summary
    _save(df, SUMMARY_FILE)

    return summary
