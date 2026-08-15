from celery import Celery
from app.core.config import settings

if settings.REDIS_URL and settings.REDIS_URL.startswith(("redis://", "rediss://")):
    broker_url = settings.REDIS_URL
    backend_url = settings.REDIS_URL
else:
    broker_url = "memory://"
    backend_url = "cache+memory://"

celery_app = Celery(
    "saas_backend",
    broker=broker_url,
    backend=backend_url,
    include=["app.tasks.example_tasks"]
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)