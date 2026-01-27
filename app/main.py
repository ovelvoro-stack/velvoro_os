from fastapi import FastAPI
from app.api.daily_summary_routes import router

app = FastAPI(title="Velvoro Daily OS")

app.include_router(router, prefix="/daily-summary")

@app.get("/")
def health():
    return {"status": "Velvoro Daily OS running"}
