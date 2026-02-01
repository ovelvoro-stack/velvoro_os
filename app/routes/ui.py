# app/routes/ui.py

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/dashboard", response_class=HTMLResponse)
def dashboard_page(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@router.get("/application", response_class=HTMLResponse)
def application_page(request: Request):
    return templates.TemplateResponse("application.html", {"request": request})

@router.get("/product", response_class=HTMLResponse)
def product_page(request: Request):
    return templates.TemplateResponse("product.html", {"request": request})

@router.get("/reports", response_class=HTMLResponse)
def reports_page(request: Request):
    return templates.TemplateResponse("reports.html", {"request": request})

@router.get("/admin", response_class=HTMLResponse)
def admin_page(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})

@router.get("/employee", response_class=HTMLResponse)
def employee_page(request: Request):
    return templates.TemplateResponse("employee.html", {"request": request})

@router.get("/manager", response_class=HTMLResponse)
def manager_page(request: Request):
    return templates.TemplateResponse("manager.html", {"request": request})
