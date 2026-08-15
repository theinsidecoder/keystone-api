from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from app.api.v1.api import api_router
from app.core.config import settings
from app.core.logging import setup_logging
from app.db.init_db import init_db
import logging

setup_logging()
logger = logging.getLogger(__name__)

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="SaaS Backend API",
    description="Production-style SaaS backend with auth, payments, caching, background jobs, rate limiting, logging, and testing.",
    version="1.0.0",
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

@app.on_event("startup")
async def startup_event():
    await init_db()
    logger.info("Application started")

@app.get("/")
@limiter.limit("5/minute")
async def root(request):
    return {"message": "Welcome to SaaS Backend API"}