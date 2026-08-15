from fastapi import APIRouter, BackgroundTasks, Depends
from app.tasks.example_tasks import send_welcome_email
from app.api.deps import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/send-welcome-email")
async def trigger_welcome_email(
    background_tasks: BackgroundTasks,
    current_user: User = Depends(get_current_user)
):
    send_welcome_email.delay(current_user.email, current_user.full_name)
    return {"message": "Welcome email queued"}