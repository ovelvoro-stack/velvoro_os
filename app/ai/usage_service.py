import pandas as pd
from pathlib import Path
from datetime import datetime
from app.billing.billing_service import PLANS, get_company

BASE = Path("data")
BASE.mkdir(exist_ok=True)
USAGE_FILE = BASE / "ai_usage.xlsx"

def _load():
    if USAGE_FILE.exists():
        return pd.read_excel(USAGE_FILE)
    return pd.DataFrame(columns=["company", "date", "requests", "tokens"])

def track(company: str, tokens: int):
    df = _load()
    today = datetime.utcnow().date()
    row = df[(df.company == company) & (df.date == today)]
    if row.empty:
        df.loc[len(df)] = [company, today, 1, tokens]
    else:
        i = row.index[0]
        df.at[i, "requests"] += 1
        df.at[i, "tokens"] += tokens
    df.to_excel(USAGE_FILE, index=False)

def allowed(company: str, tokens: int) -> bool:
    c = get_company(company)
    plan = c["plan"]
    limit = PLANS[plan]["ai_limit"]
    df = _load()
    total = df[df.company == company]["tokens"].sum() if not df.empty else 0
    return (total + tokens) <= limit
