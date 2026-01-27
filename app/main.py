from fastapi import FastAPI
from app.api.daily_summary_routes import router as daily_summary_router

app = FastAPI(
    title="Velvoro Daily OS",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"status": "Velvoro Daily OS backend running"}

# 🔥 VERY IMPORTANT
app.include_router(daily_summary_router)
