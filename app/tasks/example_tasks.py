from celery import shared_task
from app.core.celery_app import celery_app
import logging

logger = logging.getLogger(__name__)

@celery_app.task(name="send_welcome_email")
def send_welcome_email(email: str, full_name: str):
    logger.info(f"Sending welcome email to {email} for {full_name}")
    return f"Welcome email sent to {email}"