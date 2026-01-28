from fastapi import Request, HTTPException
import pandas as pd

USERS = "data/users.xlsx"

async def require_role(request: Request, roles: list):
    headers = request.headers
    company_id = headers.get("x-company-id")
    username = headers.get("x-username")

    if not company_id or not username:
        raise HTTPException(status_code=401, detail="Auth headers missing")

    df = pd.read_excel(USERS)
    user = df[
        (df["company_id"] == company_id) &
        (df["username"] == username)
    ]

    if user.empty or user.iloc[0]["role"] not in roles:
        raise HTTPException(status_code=403, detail="Access denied")
