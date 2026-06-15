import logging
from pathlib import Path
from functools import lru_cache
from typing import ClassVar

from pydantic_settings import BaseSettings, SettingsConfigDict

logger = logging.getLogger(__name__)

CURRENT_DIR = Path(__file__).resolve().parent      # root/src/common
SRC_DIR = CURRENT_DIR.parent                       # root/src
PROJECT_ROOT = Path(__file__).resolve().parents[2]                     # root   

class Settings(BaseSettings):
    APP_NAME: str = "My FastAPI App"
    VERSION: str
    APP_DESCRIPTION: str = "This is a sample FastAPI application with SQL Server integration."
    DB_TYPE: str = "sqlserver"  # or "mysql"
    SQLITE_DB_PATH: str = "mydatabase.db"
    DB_SERVER: str
    DB_DATABASE: str
    DB_USERNAME: str
    DB_PASSWORD: str
    # items_per_user: int = 50
    # debug_mode: bool = False

    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env",
        env_file_encoding="utf-8"
    )

@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    logger.info("Settings loaded successfully.")
    return settings