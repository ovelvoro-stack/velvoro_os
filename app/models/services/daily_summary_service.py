import pandas as pd
from datetime import datetime
import os

TASKS = "data/tasks.xlsx"
SUMMARY = "data/daily_summary.xlsx"

def generate_daily_summary():
    if not os.path.exists(TASKS):
        return
    df = pd.read_excel(TASKS)
    summary = df.groupby("company_id").agg(
        total_tasks=("task_id","count"),
        approved_tasks=("status", lambda x: (x=="approved").sum()),
        pending_tasks=("status", lambda x: (x=="pending").sum())
    ).reset_index()
    summary["date"] = datetime.now().date()
    summary["generated_at"] = datetime.now()
    os.makedirs("data", exist_ok=True)
    try:
        existing = pd.read_excel(SUMMARY)
        final = pd.concat([existing, summary])
    except:
        final = summary
    final.to_excel(SUMMARY, index=False)
