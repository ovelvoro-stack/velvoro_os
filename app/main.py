from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.auth.routes import auth_router
from app.billing.billing_routes import billing_router

app = FastAPI()

@app.get("/")
def root():
    return RedirectResponse(url="/login")

@app.get("/login")
def login_page():
    return {"status": "login endpoint active"}

app.include_router(auth_router)
app.include_router(billing_router)
