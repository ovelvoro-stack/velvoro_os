from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.models.api.employee_routes import router as employee_router
from app.models.api.manager_routes import router as manager_router
from app.models.api.daily_summary_routes import router as summary_router
from app.cron.scheduler import start_scheduler

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return {"status": "Velvoro Daily OS Running"}

app.include_router(employee_router)
app.include_router(manager_router)
app.include_router(summary_router)

start_scheduler()
