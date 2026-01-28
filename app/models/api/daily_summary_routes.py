from fastapi import APIRouter, Request
import pandas as pd
from pathlib import Path

router = APIRouter()

DATA_DIR = Path("data")
TASKS_FILE = DATA_DIR / "tasks.xlsx"

@router.get("/daily-summary")
def daily_summary(request: Request):
    if "user" not in request.session:
        return []

    company = request.session["user"]["company_name"]

    if not TASKS_FILE.exists():
        return []

    df = pd.read_excel(TASKS_FILE)
    df = df[df["company_name"] == company]

    return df.to_dict(orient="records")
