from datetime import datetime, timedelta
import pandas as pd
from pathlib import Path

BASE = Path("data")
BASE.mkdir(exist_ok=True)

COMPANY_FILE = BASE / "companies.xlsx"
PAYMENTS_FILE = BASE / "payments.xlsx"

PLANS = {
    "trial": {"days": 14, "ai_limit": 1000},
    "starter": {"days": 30, "ai_limit": 10000},
    "pro": {"days": 30, "ai_limit": 50000},
    "enterprise": {"days": 30, "ai_limit": 9999999},
}

def _load(file, cols):
    if file.exists():
        return pd.read_excel(file)
    return pd.DataFrame(columns=cols)

def get_company(company_name: str):
    df = _load(COMPANY_FILE, ["company", "plan", "plan_expiry"])
    row = df[df["company"] == company_name]
    if row.empty:
        expiry = datetime.utcnow() + timedelta(days=PLANS["trial"]["days"])
        df.loc[len(df)] = [company_name, "trial", expiry]
        df.to_excel(COMPANY_FILE, index=False)
        return {"company": company_name, "plan": "trial", "plan_expiry": expiry}
    r = row.iloc[0]
    return {"company": r["company"], "plan": r["plan"], "plan_expiry": r["plan_expiry"]}

def is_plan_active(company_name: str) -> bool:
    c = get_company(company_name)
    return datetime.utcnow() <= pd.to_datetime(c["plan_expiry"])

def upgrade_plan(company_name: str, plan: str):
    df = _load(COMPANY_FILE, ["company", "plan", "plan_expiry"])
    expiry = datetime.utcnow() + timedelta(days=PLANS[plan]["days"])
    if company_name in df["company"].values:
        df.loc[df["company"] == company_name, ["plan", "plan_expiry"]] = [plan, expiry]
    else:
        df.loc[len(df)] = [company_name, plan, expiry]
    df.to_excel(COMPANY_FILE, index=False)
    return {"company": company_name, "plan": plan, "plan_expiry": expiry}
