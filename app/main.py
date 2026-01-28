from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from app.auth.routes import auth_router

app = FastAPI()

# Templates setup
templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def root():
    return RedirectResponse(url="/login")


@app.get("/login")
def login_redirect():
    return RedirectResponse(url="/auth/login")


# ✅ TEST LOGIN PAGE (NEW – PARALLEL, SAFE)
@app.get("/login-test", response_class=HTMLResponse)
def login_test(request: Request):
    return templates.TemplateResponse(
        "login_test.html",
        {"request": request}
    )


# Existing auth routes (UNCHANGED)
app.include_router(auth_router)from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.auth.routes import auth_router

app = FastAPI()


@app.get("/")
def root():
    return RedirectResponse(url="/login")


@app.get("/login")
def login_redirect():
    return RedirectResponse(url="/auth/login")


app.include_router(auth_router)
