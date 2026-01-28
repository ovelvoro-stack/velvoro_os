from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from app.auth.auth import get_current_user
from app.auth.routes import auth_router

app = FastAPI()

app.add_middleware(
    SessionMiddleware,
    secret_key="VELVORO_SUPER_SECRET_KEY"
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth_router)

@app.get("/", response_class=HTMLResponse)
def root():
    return RedirectResponse("/login")

@app.get("/employee", response_class=HTMLResponse)
def employee_dashboard(user=Depends(get_current_user)):
    if user["role"] != "employee":
        raise HTTPException(status_code=403)
    with open("templates/employee.html") as f:
        return f.read()

@app.get("/manager", response_class=HTMLResponse)
def manager_dashboard(user=Depends(get_current_user)):
    if user["role"] != "manager":
        raise HTTPException(status_code=403)
    with open("templates/manager.html") as f:
        return f.read()
