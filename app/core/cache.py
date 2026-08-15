import json
import time
from typing import Any, Optional
from app.core.config import settings

# Try to use Redis if REDIS_URL is set; otherwise use in-memory cache
try:
    import redis.asyncio as redis
    _use_redis = True
except ImportError:
    _use_redis = False

class InMemoryCache:
    def __init__(self):
        self.store = {}

    async def get(self, key: str) -> Optional[Any]:
        item = self.store.get(key)
        if item is None:
            return None
        value, expire_at = item
        if expire_at and time.time() > expire_at:
            del self.store[key]
            return None
        return value

    async def set(self, key: str, value: Any, expire: int = 300) -> None:
        expire_at = time.time() + expire if expire > 0 else None
        self.store[key] = (value, expire_at)

    async def delete(self, key: str) -> None:
        self.store.pop(key, None)

class RedisCache:
    def __init__(self, url: str):
        self.client = redis.from_url(url, decode_responses=True)

    async def get(self, key: str) -> Optional[Any]:
        data = await self.client.get(key)
        return json.loads(data) if data else None

    async def set(self, key: str, value: Any, expire: int = 300) -> None:
        await self.client.set(key, json.dumps(value), ex=expire)

    async def delete(self, key: str) -> None:
        await self.client.delete(key)

if _use_redis and settings.REDIS_URL and settings.REDIS_URL.startswith(("redis://", "rediss://")):
    cache = RedisCache(settings.REDIS_URL)
else:
    cache = InMemoryCache()

async def get_cache(key: str) -> Optional[Any]:
    return await cache.get(key)

async def set_cache(key: str, value: Any, expire: int = 300) -> None:
    await cache.set(key, json.dumps(value), expire)

async def delete_cache(key: str) -> None:
    await cache.delete(key)