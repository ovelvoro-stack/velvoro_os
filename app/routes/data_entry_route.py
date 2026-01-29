from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/data-entry", response_class=HTMLResponse)
def data_entry_page(request: Request):
    return templates.TemplateResponse(
        "data_entry.html",
        {"request": request}
    )
