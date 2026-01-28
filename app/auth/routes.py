from fastapi import APIRouter, Form
from fastapi.responses import RedirectResponse
from app.core.jwt_utils import create_access_token
import csv

router = APIRouter()

@router.post("/login")
def login(company: str = Form(...), username: str = Form(...), password: str = Form(...)):
    with open("data/users.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["company_name"] == company and row["username"] == username and row["password"] == password:
                token = create_access_token({
                    "company": company,
                    "username": username,
                    "role": row["role"]
                })
                response = RedirectResponse("/employee/dashboard", status_code=302)
                response.set_cookie("access_token", token, httponly=True)
                return response
    return RedirectResponse("/login?error=1", status_code=302)
