import logging
from repositories.SqlServerProductRepository import SqlServerProductRepository
from common.config import Settings, get_settings
from factories.connection_factory import ConnectionFactory

logger = logging.getLogger(__name__)

settings = get_settings()

class ProductRepositoryFactory:
    @staticmethod
    def create():
        if settings.DB_TYPE == "sqlserver":
            connection = ConnectionFactory.get_connection(db_type="sqlserver")
            return SqlServerProductRepository(connection)
        raise ValueError(f"Unsupported database type: {settings.DB_TYPE}")
