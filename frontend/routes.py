from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

# Frontend router (HTML only – no backend logic touched)
router = APIRouter()

# Templates directory
templates = Jinja2Templates(directory="app/templates")


# -----------------------------
# LOGIN PAGE (HTML)
# -----------------------------
@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request}
    )


# -----------------------------
# DASHBOARD PAGE (HTML)
# -----------------------------
@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard_page(request: Request):
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request}
    )


# -----------------------------
# PRODUCT PAGE (HTML)
# -----------------------------
@router.get("/product", response_class=HTMLResponse)
async def product_page(request: Request):
    return templates.TemplateResponse(
        "product.html",
        {"request": request}
    )


# -----------------------------
# REPORTS PAGE (HTML)
# -----------------------------
@router.get("/reports", response_class=HTMLResponse)
async def reports_page(request: Request):
    return templates.TemplateResponse(
        "reports.html",
        {"request": request}
    )


# -----------------------------
# SAFE LOGOUT (FRONTEND ONLY)
# -----------------------------
@router.get("/logout")
async def logout():
    # No backend session logic touched
    return RedirectResponse(url="/login")
