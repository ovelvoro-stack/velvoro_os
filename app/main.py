from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Velvoro Daily OS",
    description="AI-based Daily Operating System",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {
        "status": "Velvoro OS backend running",
        "message": "Welcome to Velvoro Daily OS"
    }
