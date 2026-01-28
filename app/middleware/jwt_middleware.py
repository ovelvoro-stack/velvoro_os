from fastapi import Request
from fastapi.responses import JSONResponse
from jose import JWTError
from app.core.security import decode_token


class JWTMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        path = scope["path"]
        if path.startswith("/login") or path.startswith("/auth"):
            await self.app(scope, receive, send)
            return

        request = Request(scope, receive=receive)
        auth = request.headers.get("Authorization")

        if not auth or not auth.startswith("Bearer "):
            await JSONResponse({"detail": "Unauthorized"}, status_code=401)(scope, receive, send)
            return

        token = auth.split(" ")[1]

        try:
            payload = decode_token(token)
            if payload.get("type") != "access":
                raise JWTError()
            scope["user"] = payload
        except JWTError:
            await JSONResponse({"detail": "Invalid or expired token"}, status_code=401)(scope, receive, send)
            return

        await self.app(scope, receive, send)
