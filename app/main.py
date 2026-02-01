from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import requests

# ONLY ADDITION
from app.routes import ui
from app.routes import application

app = FastAPI()

# ONLY ADDITION
app.include_router(ui.router)
app.include_router(application.router)

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
# LOGIN SUBMIT HANDLER
# =========================
@app.post("/login", response_class=HTMLResponse)
def login_submit(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    if username == "admin" and password == "admin123":
        return RedirectResponse(url="/dashboard", status_code=302)

    return templates.TemplateResponse(
        "login.html",
        {"request": request, "error": "Invalid credentials"}
    )

# =========================
# DASHBOARD PAGE
# =========================
@app.get("/dashboard", response_class=HTMLResponse)
def dashboard_page(request: Request):
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request}
    )
