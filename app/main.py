from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from app.auth.routes import auth_router

app = FastAPI()

# Templates setup
templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def root():
    return RedirectResponse(url="/login-test")


@app.get("/login-test", response_class=HTMLResponse)
def login_test(request: Request):
    return templates.TemplateResponse(
        "login_test.html",
        {"request": request}
    )


# Existing auth routes (DO NOT REMOVE)
app.include_router(auth_router)
