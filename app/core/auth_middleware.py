from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.jwt_utils import verify_token

PUBLIC_PATHS = ["/login"]

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path in PUBLIC_PATHS:
            return await call_next(request)

        token = request.cookies.get("access_token")
        payload = verify_token(token) if token else None

        if not payload:
            from fastapi.responses import RedirectResponse
            return RedirectResponse("/login")

        request.state.user = payload
        return await call_next(request)
