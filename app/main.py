from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.auth.routes import auth_router
from app.middleware.jwt_middleware import JWTMiddleware

app = FastAPI()

app.add_middleware(JWTMiddleware)

@app.get("/")
def root():
    return RedirectResponse(url="/login")

app.include_router(auth_router)
