from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/employee/dashboard")
def employee_dashboard(request: Request):
    return templates.TemplateResponse("employee.html", {"request": request})

@router.get("/manager/dashboard")
def manager_dashboard(request: Request):
    return templates.TemplateResponse("manager.html", {"request": request})

@router.get("/admin/dashboard")
def admin_dashboard(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})
