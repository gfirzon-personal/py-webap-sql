import logging
from repositories.SqlServerProductRepository import SqlServerProductRepository
from common.config import Settings, get_settings

logger = logging.getLogger(__name__)

settings = get_settings()

class ProductRepositoryFactory:
    @staticmethod
    def create():
        if settings.DB_TYPE == "sqlserver":
            return SqlServerProductRepository()
        raise ValueError(f"Unsupported database type: {settings.DB_TYPE}")
