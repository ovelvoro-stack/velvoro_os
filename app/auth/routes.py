from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse

auth_router = APIRouter()

USERS = {
    "employee1": {"password": "1234", "role": "employee"},
    "manager1": {"password": "admin", "role": "manager"}
}

@auth_router.get("/login", response_class=HTMLResponse)
def login_page():
    with open("templates/login.html") as f:
        return f.read()

@auth_router.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    user = USERS.get(username)
    if not user or user["password"] != password:
        return HTMLResponse("<h3>Invalid credentials</h3>", status_code=401)

    request.session["user"] = {"username": username, "role": user["role"]}
    return RedirectResponse(f"/{user['role']}", status_code=302)

@auth_router.get("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/login")
