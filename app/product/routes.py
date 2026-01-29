from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/product/templates")

router = APIRouter(prefix="/product", tags=["Product"])

@router.get("/home", response_class=HTMLResponse)
def product_home(request: Request):
    return templates.TemplateResponse(
        "product_home.html",
        {"request": request}
    )
