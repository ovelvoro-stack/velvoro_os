from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import requests

# ✅ ONLY ADDITION – import router
from app.routes import ui

app = FastAPI()

# ✅ ONLY ADDITION – include router
app.include_router(ui.router)

templates = Jinja2Templates(directory="app/templates")

# =========================
# UI LOGIN PAGE
# =========================
@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request, "error": None}
    )

# =========================
# LOGIN FORM SUBMIT
# =========================
@app.post("/login", response_class=HTMLResponse)
def login_submit(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    try:
        # Call existing backend login API (UNCHANGED)
        response = requests.post(
            "http://localhost:8000/auth/login",
            json={
                "username": username,
                "password": password
            }
        )

        if response.status_code == 200:
            return RedirectResponse(
                url="/dashboard",
                status_code=302
            )

        return templates.TemplateResponse(
            "login.html",
            {
                "request": request,
                "error": "Invalid username or password"
            }
        )

    except Exception:
        return templates.TemplateResponse(
            "login.html",
            {
                "request": request,
                "error": "Server error. Please try again."
            }
        )
