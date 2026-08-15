import json
import time
from typing import Any, Optional

# Simple in-memory cache (development only)
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

# Use in-memory cache for development
cache = InMemoryCache()

async def get_cache(key: str) -> Optional[Any]:
    return await cache.get(key)

async def set_cache(key: str, value: Any, expire: int = 300) -> None:
    # Store JSON string for consistency with Redis version
    await cache.set(key, json.dumps(value), expire)

async def delete_cache(key: str) -> None:
    await cache.delete(key)