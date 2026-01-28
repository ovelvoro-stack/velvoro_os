from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from app.auth.routes import auth_router

app = FastAPI()

# ✅ FIX: correct templates directory (NOT app/templates)
templates = Jinja2Templates(directory="templates")


@app.get("/")
def root():
    return RedirectResponse(url="/login")


@app.get("/login")
def login_redirect():
    return RedirectResponse(url="/auth/login")


# ✅ PARALLEL SAFE TEST PAGE
@app.get("/login-test", response_class=HTMLResponse)
def login_test(request: Request):
    return templates.TemplateResponse(
        "login_test.html",
        {"request": request}
    )


# existing auth routes
app.include_router(auth_router)
