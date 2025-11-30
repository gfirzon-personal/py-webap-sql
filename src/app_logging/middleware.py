# middleware.py
import uuid
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from .context import custom_value_ctx

class CustomValueMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Example: from header
        correlation_id = str(uuid.uuid4())

        value = request.headers.get("X-Custom-Value", correlation_id)
        token = custom_value_ctx.set(value)
        response = await call_next(request)
        custom_value_ctx.reset(token)
        return response