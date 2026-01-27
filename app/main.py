from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.auth_routes import router as auth_router
from app.api.task_routes import router as task_router
from app.api.followup_routes import router as followup_router
from app.api.summary_routes import router as summary_router

app = FastAPI(title="Velvoro Daily OS")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(task_router, prefix="/tasks", tags=["Tasks"])
app.include_router(followup_router, prefix="/followups", tags=["Followups"])
app.include_router(summary_router, prefix="/daily-summary", tags=["Daily Summary"])

@app.get("/")
def health():
    return {"status": "Velvoro Daily OS running"}
