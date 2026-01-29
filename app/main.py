from fastapi import FastAPI
from fastapi.responses import RedirectResponse

# existing routers (ALREADY IN YOUR APP)
from app.auth.routes import router as auth_router
from app.roles.routes import router as roles_router
from app.dashboard.routes import router as dashboard_router
from app.reports.routes import router as reports_router

# NEW PRODUCT ROUTER
from app.product.routes import router as product_router

app = FastAPI()

# ROOT → LOGIN (PRODUCTION SAFE)
@app.get("/")
def root():
    return RedirectResponse(url="/auth/login")

# ROUTERS (NO LOGIC CHANGE)
app.include_router(auth_router)
app.include_router(roles_router)
app.include_router(dashboard_router)
app.include_router(reports_router)

# PRODUCT FLOW ROUTER (FINAL ADD)
app.include_router(product_router)
