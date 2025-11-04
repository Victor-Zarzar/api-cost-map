from fastapi import FastAPI
from app.api.routers import costs
from app.config.settings import settings
from app.config.logger_settings import logger
import logging

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    debug=settings.DEBUG,
)

# Logs (Logger)
logger.info("Logger loaded successfully!")
logging.getLogger("slowapi").setLevel(logging.WARNING)


# Routes
app.include_router(costs.router, prefix="/costs", tags=["Costs"])
