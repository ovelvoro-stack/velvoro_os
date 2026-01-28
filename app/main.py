from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.auth.routes import auth_router

app = FastAPI()


@app.get("/")
def root():
    return RedirectResponse(url="/login")


@app.get("/login")
def login_redirect():
    return RedirectResponse(url="/auth/login")


app.include_router(auth_router)
