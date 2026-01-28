import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")
USERS_FILE = DATA_DIR / "users.xlsx"

def authenticate_user(company, username, password):
    if not USERS_FILE.exists():
        return None

    df = pd.read_excel(USERS_FILE)

    user = df[
        (df["company_name"] == company) &
        (df["username"] == username) &
        (df["password"] == password) &
        (df["active_status"] == "active")
    ]

    if user.empty:
        return None

    return user.iloc[0].to_dict()
