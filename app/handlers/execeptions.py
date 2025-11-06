from fastapi import Request
from fastapi.responses import JSONResponse
from slowapi.errors import RateLimitExceeded


def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
    retry_after = request.state.view_rate_limit_reset if hasattr(
        request.state, "view_rate_limit_reset") else None
    headers = {
        "Retry-After": str(int(retry_after)) if retry_after else "60",
        "X-RateLimit-Limit": getattr(request.state, "view_rate_limit_limit", "") or "",
        "X-RateLimit-Remaining": getattr(request.state, "view_rate_limit_remaining", "") or "",
        "X-RateLimit-Reset": str(int(retry_after)) if retry_after else "",
    }

    headers = {k: v for k, v in headers.items() if v}

    return JSONResponse(
        status_code=429,
        content={
            "detail": "Too Many Requests",
            "error": "rate_limit_exceeded",
            "hint": "Aguarde e tente novamente.",
        },
        headers=headers,
    )
