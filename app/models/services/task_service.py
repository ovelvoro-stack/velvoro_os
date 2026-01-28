import pandas as pd
from pathlib import Path
from datetime import datetime

DATA_DIR = Path("data")
TASKS_FILE = DATA_DIR / "tasks.xlsx"

def save_task(company, user, task):
    df = pd.DataFrame([{
        "company_name": company,
        "user": user,
        "task": task,
        "date": datetime.now(),
        "status": "pending"
    }])

    if TASKS_FILE.exists():
        old = pd.read_excel(TASKS_FILE)
        df = pd.concat([old, df], ignore_index=True)

    df.to_excel(TASKS_FILE, index=False)
