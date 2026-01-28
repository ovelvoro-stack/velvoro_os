# File name: main.py
# File path: app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routers (IMPORTS MATCH ACTUAL STRUCTURE)
from app.models.api.daily_summary_routes import router as daily_summary_router
from app.models.api.task_routes import router as task_router
from app.models.api.followup_routes import router as followup_router
from app.auth.login_routes import router as login_router

app = FastAPI(title="Velvoro Daily OS")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root health check
@app.get("/")
def root():
    return {"status": "ok", "service": "Velvoro Daily OS"}

# Routers
app.include_router(login_router, prefix="/auth", tags=["Auth"])
app.include_router(daily_summary_router, prefix="/daily-summary", tags=["Daily Summary"])
app.include_router(task_router, prefix="/tasks", tags=["Tasks"])
app.include_router(followup_router, prefix="/followups", tags=["Followups"])
