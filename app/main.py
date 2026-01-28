from fastapi import FastAPI

# existing imports (unchanged)
from app.models.api.daily_summary_routes import router as daily_summary_router
from app.models.api.task_routes import router as task_router
from app.models.api.followup_routes import router as followup_router
from app.models.auth.login_routes import router as login_router

app = FastAPI()

# NEW: root health / welcome endpoint (additive only)
@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "Velvoro Daily OS",
        "message": "Backend is live"
    }

# existing router includes (unchanged)
app.include_router(daily_summary_router)
app.include_router(task_router)
app.include_router(followup_router)
app.include_router(login_router)
