import pandas as pd
import os

USERS_FILE = "data/users.xlsx"

def authenticate_user(username: str, password: str):
    if not os.path.exists(USERS_FILE):
        return None

    df = pd.read_excel(USERS_FILE)

    user = df[
        (df["username"] == username) &
        (df["password"] == password) &
        (df["active"] == True)
    ]

    if user.empty:
        return None

    row = user.iloc[0]
    return {
        "user_id": row["user_id"],
        "name": row["name"],
        "role": row["role"]
    }
