import logging
from common.config import Settings, get_settings
from factories.connection_factory import ConnectionFactory
from repositories.SqlLiteProductRepository import SqlLiteProductRepository
from repositories.SqlServerProductRepository import SqlServerProductRepository

logger = logging.getLogger(__name__)

settings = get_settings()

class ProductRepositoryFactory:
    @staticmethod
    def create():
        if settings.DB_TYPE == "sqlserver":
            connection = ConnectionFactory.get_connection(db_type="sqlserver")
            return SqlServerProductRepository(connection)
        elif settings.DB_TYPE == "sqlite":
            connection = ConnectionFactory.get_connection(db_type="sqlite")
            return SqlLiteProductRepository(connection)
        raise ValueError(f"Unsupported database type: {settings.DB_TYPE}")
