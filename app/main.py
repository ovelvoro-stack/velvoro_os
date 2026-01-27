from fastapi import FastAPI
from app.api.daily_summary_routes import router as daily_summary_router

app = FastAPI(title="Velvoro Daily OS")

app.include_router(daily_summary_router, prefix="/daily")

@app.get("/")
def root():
    return {"status": "Velvoro Daily OS running"}
