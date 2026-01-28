import pandas as pd
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "data")
USERS_FILE = os.path.join(DATA_DIR, "users.csv")


def _load_users_df():
    if not os.path.exists(USERS_FILE):
        return pd.DataFrame(columns=["username", "password", "role", "company"])
    return pd.read_csv(USERS_FILE)


def get_user(username: str):
    df = _load_users_df()
    user = df[df["username"] == username]
    if user.empty:
        return None
    return user.iloc[0].to_dict()


# 🔴 REQUIRED ALIAS — DO NOT REMOVE
# This fixes ImportError in app/auth/routes.py
def get_user_by_credentials(username: str, password: str):
    user = get_user(username)
    if not user:
        return None
    if str(user.get("password")) != str(password):
        return None
    return user
