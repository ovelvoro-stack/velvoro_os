from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.auth.routes import auth_router
from app.routes.data_entry_route import router as data_entry_router

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

# EXISTING ROUTES (DO NOT TOUCH)
app.include_router(auth_router)
app.include_router(data_entry_router)

# LIVE PRODUCTION UI PAGE
@app.get("/portal", response_class=HTMLResponse)
async def live_portal(request: Request):
    return templates.TemplateResponse(
        "live_portal.html",
        {"request": request}
    )
