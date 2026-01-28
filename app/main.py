from fastapi import FastAPI

from app.models.api.employee_routes import router as employee_router
from app.models.api.manager_routes import router as manager_router
from app.models.api.rules_routes import router as rules_router

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Velvoro Daily OS Running"}

app.include_router(employee_router)
app.include_router(manager_router)
app.include_router(rules_router)
