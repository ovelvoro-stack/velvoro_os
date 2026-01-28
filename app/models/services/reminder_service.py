import pandas as pd
from datetime import datetime
import os

FOLLOWUPS_FILE = "data/followups.xlsx"

def pending_reminders():
    if not os.path.exists(FOLLOWUPS_FILE):
        return []

    df = pd.read_excel(FOLLOWUPS_FILE)
    today = datetime.now().date()

    pending = df[
        (df["status"] == "pending") &
        (pd.to_datetime(df["due_date"]).dt.date <= today)
    ]

    return pending.to_dict(orient="records")
