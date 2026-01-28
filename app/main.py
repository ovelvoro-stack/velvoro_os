from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.auth.routes import auth_router

app = FastAPI()

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/login")

app.include_router(auth_router)
