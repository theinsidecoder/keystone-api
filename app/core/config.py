from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    STRIPE_SECRET_KEY: str
    STRIPE_WEBHOOK_SECRET: str
    ENVIRONMENT: str = "development"
    LOG_LEVEL: str = "INFO"

    # Pydantic v2 modern configuration layout
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore"  # Keeps things stable if extra variables are in your .env
    )

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
