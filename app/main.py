from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from app.models.api.login_routes import router as login_router
from app.models.api.protected_routes import router as protected_router
from app.models.api.daily_summary_routes import router as daily_summary_router

app = FastAPI()

app.add_middleware(
    SessionMiddleware,
    secret_key="VELVORO_SECRET_KEY"
)

@app.get("/")
def root():
    return {"status": "Velvoro Daily OS Running"}

app.include_router(login_router)
app.include_router(protected_router)
app.include_router(daily_summary_router)
