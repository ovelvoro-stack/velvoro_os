from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse

router = APIRouter()

def require_login(request: Request):
    if "user" not in request.session:
        return False
    return True

@router.get("/employee", response_class=HTMLResponse)
def employee_page(request: Request):
    if not require_login(request):
        return RedirectResponse("/login")

    user = request.session["user"]
    return f"""
    <h2>Employee Dashboard</h2>
    <p>Company: {user['company_name']}</p>
    <p>Name: {user['employee_name']}</p>
    """

@router.get("/manager", response_class=HTMLResponse)
def manager_page(request: Request):
    if not require_login(request):
        return RedirectResponse("/login")

    user = request.session["user"]
    return f"""
    <h2>Manager Dashboard</h2>
    <p>Company: {user['company_name']}</p>
    <p>Name: {user['employee_name']}</p>
    """
