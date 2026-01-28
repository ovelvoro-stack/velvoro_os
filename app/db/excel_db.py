import pandas as pd
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
USERS_FILE = os.path.join(DATA_DIR, "users.csv")


def _load_users_df():
    if not os.path.exists(USERS_FILE):
        return pd.DataFrame(columns=["username", "password", "role", "company"])
    return pd.read_csv(USERS_FILE)


def _save_users_df(df: pd.DataFrame):
    os.makedirs(DATA_DIR, exist_ok=True)
    # 🔴 FIX: Use CSV writer only (NO ExcelWriter / openpyxl)
    df.to_csv(USERS_FILE, index=False)


def get_user(username: str):
    df = _load_users_df()
    user = df[df["username"] == username]
    if user.empty:
        return None
    return user.iloc[0].to_dict()


def get_user_by_credentials(username: str, password: str):
    df = _load_users_df()
    user = df[(df["username"] == username) & (df["password"] == password)]
    if user.empty:
        return None
    return user.iloc[0].to_dict()


def create_or_update_user(user_data: dict):
    df = _load_users_df()
    df = df[df["username"] != user_data["username"]]
    df = pd.concat([df, pd.DataFrame([user_data])], ignore_index=True)
    _save_users_df(df)
    return True
