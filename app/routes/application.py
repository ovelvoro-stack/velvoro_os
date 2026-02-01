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

@router.post("/application/submit")
def submit_application(
    customer_name: str = Form(...),
    mobile: str = Form(...),
    email: str = Form(...),
    location: str = Form(...),
    details: str = Form("")
):
    # Data captured together (single submit)
    print(customer_name, mobile, email, location, details)

    return RedirectResponse(
        url="/dashboard",
        status_code=303
    )
