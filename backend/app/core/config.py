from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
import os


class appConfig(BaseSettings):
    app_name: str = "dealRescueAgent"
    app_env: str = "development"
    database_url: str = ""
    groq_api_key: str = ""
    email: str = ""
    password: str = ""
    secret_key: str = "changeme"
    access_token_expire_minutes: int = 30

    # In production (Render), env vars are injected directly.
    # In local dev, load from .env file at project root.
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(__file__), "..", "..", ".env"),
        extra="ignore",
    )


@lru_cache
def getAppConfig():
    return appConfig()