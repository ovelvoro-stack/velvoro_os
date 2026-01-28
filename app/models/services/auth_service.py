import pandas as pd

USERS = "data/users.xlsx"

def authenticate(company_id: str, username: str, password: str):
    try:
        df = pd.read_excel(USERS)
        user = df[
            (df["company_id"] == company_id) &
            (df["username"] == username) &
            (df["password"] == password)
        ]
        if user.empty:
            return None
        row = user.iloc[0]
        return {
            "company_id": row["company_id"],
            "username": row["username"],
            "role": row["role"]
        }
    except:
        return None
