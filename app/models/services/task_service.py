import pandas as pd
from datetime import datetime
import os
import uuid

DATA_FILE = "data/tasks.xlsx"

def add_task(company_id: str, employee: str, task: str):
    os.makedirs("data", exist_ok=True)
    try:
        df = pd.read_excel(DATA_FILE)
    except:
        df = pd.DataFrame(columns=[
            "company_id","task_id","employee","task","status","created_at"
        ])
    df.loc[len(df)] = [
        company_id, str(uuid.uuid4()), employee, task, "pending", datetime.now()
    ]
    df.to_excel(DATA_FILE, index=False)

def list_tasks(company_id: str):
    try:
        df = pd.read_excel(DATA_FILE)
        return df[df["company_id"] == company_id].to_dict(orient="records")
    except:
        return []

def approve_task(task_id: str):
    df = pd.read_excel(DATA_FILE)
    df.loc[df["task_id"] == task_id, "status"] = "approved"
    df.to_excel(DATA_FILE, index=False)
