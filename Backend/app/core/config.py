from functools import lru_cache

from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

#ENV_FILE =  Path(__file__).resolve().parents[1]/".env"

class appConfig(BaseSettings):
    app_name:str
    app_env:str
    database_url:str
    groq_api_key:str

    # Load the project root .env and ignore unrelated keys.
    model_config = SettingsConfigDict(env_file=".env" , extra="ignore")


@lru_cache
def getAppConfig():
    return appConfig()

getAppConfig.cache_clear()