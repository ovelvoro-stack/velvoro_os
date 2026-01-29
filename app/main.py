# app/main.py
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

# existing routers (ALREADY IN YOUR APP)
from app.auth.routes import router as auth_router
from app.roles.routes import router as roles_router
from app.dashboard.routes import router as dashboard_router
from app.reports.routes import router as reports_router
from app.product.routes import router as product_router

# ✅ MINIMAL ADD ONLY (FRONTEND)
from app.frontend.routes import router as frontend_router

app = FastAPI()

@app.get("/")
def root():
    return RedirectResponse(url="/login")

# existing routers (NO CHANGE)
app.include_router(auth_router)
app.include_router(roles_router)
app.include_router(dashboard_router)
app.include_router(reports_router)
app.include_router(product_router)

# ✅ frontend router include (ONLY ADD)
app.include_router(frontend_router)
