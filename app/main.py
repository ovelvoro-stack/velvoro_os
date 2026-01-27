from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ✅ FIRST create app (very important)
app = FastAPI(title="Velvoro Daily OS")

# ✅ Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Imports AFTER app init (prevents NameError)
from app.models.api.daily_summary_routes import router as daily_summary_router
from app.models.api.task_routes import router as task_router
from app.models.api.followup_routes import router as followup_router
from app.models.auth.login_routes import router as login_router
from app.models.api.ai_routes import router as ai_router

# ✅ Router includes
app.include_router(login_router, prefix="/auth", tags=["Auth"])
app.include_router(daily_summary_router, prefix="/daily-summary", tags=["Daily Summary"])
app.include_router(task_router, prefix="/tasks", tags=["Tasks"])
app.include_router(followup_router, prefix="/followups", tags=["Followups"])
app.include_router(ai_router, prefix="/system", tags=["AI"])

@app.get("/")
def root():
    return {"status": "Velvoro Daily OS running"}
