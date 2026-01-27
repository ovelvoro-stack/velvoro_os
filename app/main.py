from fastapi import FastAPI
from app.models.api.daily_summary_routes import router as daily_summary_router

app = FastAPI(title="Velvoro Daily OS")

app.include_router(
    daily_summary_router,
    prefix="/daily-summary",
    tags=["Daily Summary"]
)

@app.get("/")
def root():
    return {"status": "Velvoro Daily OS running"}
