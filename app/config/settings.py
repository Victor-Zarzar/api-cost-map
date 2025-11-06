import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List


# Function to search for .env
def get_env_file():
    env = os.getenv('ENVIRONMENT', 'development')
    if env == 'production':
        return '.env.prod'
    return '.env.dev'


class Settings(BaseSettings):

    # App Info
    ENVIRONMENT: str
    DEBUG: bool
    APP_NAME: str

    # Auth
    SECRET_KEY: str

    # Rate Limiting
    ENABLE_RATE_LIMITER: bool = False
    RATE_LIMIT_REQUESTS: int
    RATE_LIMIT_WINDOW: int

    # MySQL
    MYSQL_ROOT_PASSWORD: str
    MYSQL_DATABASE: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str

    # Database
    DATABASE_URL: str
    DATABASE_HOST: str
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASS: str

    # CORS
    ALLOWED_ORIGINS: List[str]

    # Rate Limiting
    RATE_LIMIT_REQUESTS: int
    RATE_LIMIT_WINDOW: int

    # Logs
    LOG_LEVEL: str

    model_config = SettingsConfigDict(
        env_file=get_env_file(),
        env_file_encoding='utf-8'
    )


settings = Settings()
