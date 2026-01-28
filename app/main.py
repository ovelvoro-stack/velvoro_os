from fastapi import FastAPI
from app.auth.routes import auth_router
from app.manager.routes import manager_router
from app.admin.routes import admin_router
from app.employee.routes import employee_router

app = FastAPI(title="Velvoro Daily OS")

app.include_router(auth_router)
app.include_router(manager_router)
app.include_router(admin_router)
app.include_router(employee_router)
