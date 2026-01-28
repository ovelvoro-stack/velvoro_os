from fastapi import APIRouter
import pandas as pd

router = APIRouter()

@router.get("/daily-summary/")
def get_summary():
    try:
        return pd.read_excel("data/daily_summary.xlsx").to_dict(orient="records")
    except:
        return []
