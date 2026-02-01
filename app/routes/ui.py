from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import httpx

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request, error: str = None):
    return templates.TemplateResponse(
        "login.html",
        {"request": request, "error": error}
    )


@router.post("/login")
async def login_submit(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://localhost:10000/auth/login",  # 🔁 same backend API
            json={"username": username, "password": password}
        )

    if response.status_code == 200:
        return RedirectResponse(url="/dashboard", status_code=302)

    return RedirectResponse(
        url="/login?error=Invalid+credentials",
        status_code=302
    )
