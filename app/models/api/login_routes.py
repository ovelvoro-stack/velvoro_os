from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from starlette.middleware.sessions import SessionMiddleware
from app.models.services.auth_service import authenticate_user

router = APIRouter()

@router.get("/login", response_class=HTMLResponse)
def login_page():
    return """
    <html>
    <body>
        <h2>Velvoro Daily OS Login</h2>
        <form method="post">
            Company: <input name="company"><br><br>
            Username: <input name="username"><br><br>
            Password: <input type="password" name="password"><br><br>
            <button type="submit">Login</button>
        </form>
    </body>
    </html>
    """

@router.post("/login")
def login(request: Request,
          company: str = Form(...),
          username: str = Form(...),
          password: str = Form(...)):

    user = authenticate_user(company, username, password)

    if not user:
        return HTMLResponse("Invalid credentials", status_code=401)

    request.session["user"] = user

    if user["role"] == "manager":
        return RedirectResponse("/manager", status_code=302)

    return RedirectResponse("/employee", status_code=302)
