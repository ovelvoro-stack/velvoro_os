from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.auth.routes import auth_router
from app.routes.data_entry_route import router as data_entry_router

app = FastAPI()

@app.get("/")
def root():
    return RedirectResponse(url="/login")

app.include_router(auth_router)
app.include_router(data_entry_router)
