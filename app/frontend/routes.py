from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# LOGIN PAGE (UI ONLY)
@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request}
    )

# DASHBOARD PAGE (UI ONLY)
@router.get("/dashboard", response_class=HTMLResponse)
def dashboard_page(request: Request):
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request}
    )

# PRODUCT PAGE (UI ONLY)
@router.get("/product", response_class=HTMLResponse)
def product_page(request: Request):
    return templates.TemplateResponse(
        "product.html",
        {"request": request}
    )

# REPORTS PAGE (UI ONLY)
@router.get("/reports", response_class=HTMLResponse)
def reports_page(request: Request):
    return templates.TemplateResponse(
        "reports.html",
        {"request": request}
    )

# SAFE ROOT REDIRECT (OPTIONAL UI FLOW)
@router.get("/", include_in_schema=False)
def root_redirect():
    return RedirectResponse(url="/login")
