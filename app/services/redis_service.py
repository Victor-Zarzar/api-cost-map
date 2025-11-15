import redis.asyncio as redis

from app.core.config import settings


class RedisManager:
    def __init__(self) -> None:
        self.pool = redis.ConnectionPool(
            host=settings.REDIS_LOCATION,
            port=settings.REDIS_PORT,
            decode_responses=True,
        )

    def get_client(self) -> redis.Redis:
        return redis.Redis(connection_pool=self.pool)

    async def check_if_jwt_exists(self, token: str) -> bool:
        conn = self.get_client()
        result = await conn.exists(token)
        return bool(result)
