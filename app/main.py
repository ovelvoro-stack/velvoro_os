from fastapi import FastAPI
from app.api.employee_routes import router as employee_router
from app.api.manager_routes import router as manager_router
from app.api.summary_routes import router as summary_router

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Velvoro Daily OS Running"}

app.include_router(employee_router)
app.include_router(manager_router)
app.include_router(summary_router)
