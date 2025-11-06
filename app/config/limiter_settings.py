from fastapi import FastAPI
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded
from app.services.rate_limiter_service import limiter
from app.handlers.execeptions import rate_limit_exceeded_handler
from app.config.logger_settings import logger


def setup_rate_limiter(app: FastAPI, enabled: bool = True) -> None:
    """
    Configures the rate limiter in the FastAPI application.
    """
    if not enabled:
        logger.info("Rate limiter disabled by configuration")
        return

    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler)
    app.add_middleware(SlowAPIMiddleware)
    logger.info("Rate limiter configured and active")
