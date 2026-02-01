# app/routes/application.py

from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/application", response_class=HTMLResponse)
def application_form(request: Request):
    return templates.TemplateResponse(
        "application.html",
        {"request": request}
    )


@router.post("/application")
def submit_application(
    request: Request,
    customer_name: str = Form(...),
    mobile_number: str = Form(...),
    email: str = Form(...),
    location: str = Form(...)
):
    return RedirectResponse(url="/dashboard", status_code=303)
