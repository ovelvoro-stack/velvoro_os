from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.reports.service import get_reports_data

router = APIRouter(prefix="/reports", tags=["Reports"])

templates = Jinja2Templates(directory="app/reports/templates")


def get_current_user_role():
    """
    Safe default.
    Integrates later with existing auth/session.
    """
    return "user"


@router.get("", response_class=HTMLResponse)
def reports_page(
    request: Request,
    role: str = Depends(get_current_user_role)
):
    data = get_reports_data(role)

    return templates.TemplateResponse(
        "reports.html",
        {
            "request": request,
            "role": role,
            "summary": data["summary"],
            "details": data["details"],
        }
    )
