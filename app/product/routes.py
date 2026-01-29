from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

from app.product.service import primary_action, get_empty_state
from app.product.audit import get_audit_log
from app.product.export import export_excel

router = APIRouter()
templates = Jinja2Templates(directory="app/product/templates")

@router.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    user = request.state.user
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "user": user,
            "empty_state": get_empty_state(user["role"])
        }
    )

@router.post("/action")
def do_action(request: Request):
    user = request.state.user
    return primary_action(user)

@router.get("/reports", response_class=HTMLResponse)
def reports(request: Request):
    return templates.TemplateResponse(
        "reports.html",
        {
            "request": request,
            "audit": get_audit_log()
        }
    )

@router.get("/reports/export")
def export_report():
    file = export_excel(get_audit_log())
    return FileResponse(file, filename=file)
