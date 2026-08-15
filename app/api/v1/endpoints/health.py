from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
import redis.asyncio as redis
from app.core.config import settings

router = APIRouter()

@router.get("/")
async def health_check():
    return {"status": "ok"}

@router.get("/db")
async def db_health(db: AsyncSession = Depends(get_db)):
    try:
        await db.execute(text("SELECT 1"))
        return {"database": "ok"}
    except Exception as e:
        return {"database": "error", "detail": str(e)}

@router.get("/redis")
async def redis_health():
    try:
        r = redis.from_url(settings.REDIS_URL, decode_responses=True)
        await r.ping()
        await r.close()
        return {"redis": "ok"}
    except Exception as e:
        return {"redis": "error", "detail": str(e)}