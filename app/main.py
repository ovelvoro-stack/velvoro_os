from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.billing.billing_routes import router as billing_router
from app.ai.ai_routes import router as ai_router

app = FastAPI(title="Velvoro Daily OS")

@app.get("/")
def root():
    return RedirectResponse(url="/billing/status/demo-company")

app.include_router(billing_router)
app.include_router(ai_router)
