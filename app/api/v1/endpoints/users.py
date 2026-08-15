from fastapi import APIRouter, Depends
from app.api.deps import get_current_user
from app.models.user import User
from app.schemas.user import UserOut
from app.core.cache import get_cache, set_cache

router = APIRouter()

@router.get("/me", response_model=UserOut)
async def read_users_me(current_user: User = Depends(get_current_user)):
    cache_key = f"user:{current_user.id}"
    cached = await get_cache(cache_key)
    if cached:
        return cached
    user_data = {
        "id": current_user.id,
        "email": current_user.email,
        "full_name": current_user.full_name,
        "is_active": current_user.is_active,
    }
    await set_cache(cache_key, user_data, expire=60)
    return user_data
