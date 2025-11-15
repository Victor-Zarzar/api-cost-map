from fastapi import FastAPI
from app.middlewares.cors_middleware import add_cors
from app.views import admin, auth, health, costs, users
from app.core.limiter import setup_rate_limiter
from app.core.config import settings
from app.core.logger import logger
import logging
from app.services.redis_service import RedisManager

# Redis Manager
redis = RedisManager()


app = FastAPI(
    title=settings.APP_NAME,
    description="API Cost Map Brazilian",
    version="1.0.0",
    debug=settings.DEBUG,
)

# CORS Middleware
add_cors(app)

# Logs (Logger)
logger.info("Logger loaded successfully!")
logging.getLogger("slowapi").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)

# Rate Limiter
setup_rate_limiter(app, enabled=settings.ENABLE_RATE_LIMITER)

# Routes
app.include_router(auth.router,  prefix="/api/v1/auth",  tags=["Auth"])
app.include_router(admin.router, prefix="/api/v1/admin", tags=["Admin"])
app.include_router(users.router, prefix="/api/v1", tags=["Users"])
app.include_router(costs.router, prefix="/api/v1", tags=["Costs"])
app.include_router(health.router, prefix="/api/v1", tags=["Health"])
