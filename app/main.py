from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from app.auth.routes import auth_router

app = FastAPI()

# Templates setup
templates = Jinja2Templates(directory="templates")

# Root → /login
@app.get("/")
def root():
    return RedirectResponse(url="/login")

# Existing login redirect (DO NOT TOUCH)
@app.get("/login")
def login_redirect():
    return RedirectResponse(url="/auth/login")

# ✅ TEST LOGIN PAGE (PARALLEL, SAFE)
@app.get("/login-test", response_class=HTMLResponse)
def login_test(request: Request):
    return templates.TemplateResponse(
        "login_test.html",
        {"request": request}
    )

# Auth routes
app.include_router(auth_router)
