import os
import logging

logger = logging.getLogger(__name__)

class ConnectionFactory:
    """Factory class to create database connections."""

    @staticmethod
    def get_connection():
        db_type = os.getenv('DB_TYPE', 'sqlserver').lower()
        
        if db_type == 'sqlite':
            import sqlite3
            db_path = os.getenv('SQLITE_DB_PATH', 'database.db')
            logger.info(f"Connecting to SQLite database at {db_path}")
            return sqlite3.connect(db_path)
        else:
            import pyodbc
            logger.info("Connecting to SQL Server database")
            return pyodbc.connect(ConnectionFactory.get_connection_string())


    @staticmethod
    def get_connection_string():
        return (
            "Driver={ODBC Driver 18 for SQL Server};"
            f"Server={os.getenv('DB_SERVER', 'localhost')};"
            f"Database={os.getenv('DB_DATABASE', 'N/A')};"
            f"Uid={os.getenv('DB_USERNAME', 'N/A')};"
            f"Pwd={os.getenv('DB_PASSWORD', 'N/A')};"
            "Encrypt=yes;TrustServerCertificate=yes;Connection Timeout=30;"
        )