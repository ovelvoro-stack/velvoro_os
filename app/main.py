from fastapi import FastAPI
from app.auth.routes import router as auth_router
from app.frontend.routes import router as ui_router
from app.billing.routes import router as billing_router
from app.core.auth_middleware import AuthMiddleware

app = FastAPI()

app.add_middleware(AuthMiddleware)
app.include_router(auth_router)
app.include_router(ui_router)
app.include_router(billing_router)
