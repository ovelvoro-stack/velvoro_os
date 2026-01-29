from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from app.auth.routes import auth_router

app = FastAPI()

# Templates setup (DO NOT change directory)
templates = Jinja2Templates(directory="app/templates")


# Root → redirect to login test page
@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/login-test")


# ✅ LOGIN TEST PAGE (HTML RENDER – FIXED)
@app.get("/login-test", response_class=HTMLResponse)
def login_test(request: Request):
    return templates.TemplateResponse(
        "login_test.html",
        {"request": request}
    )


# Existing auth routes (DO NOT TOUCH)
app.include_router(auth_router)
