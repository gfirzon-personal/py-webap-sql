import os

class ConnectionFactory:
    """Factory class to create database connections."""

    #------------------------------------------------------
    @staticmethod
    def get_connection():
        """Create and return a new database connection."""
        import pyodbc
        return pyodbc.connect(ConnectionFactory.get_connection_string())

    #------------------------------------------------------
    @staticmethod
    def get_connection_string() -> str:
        """
        Build and return the database connection string.
        Uses environment variables for configuration.
        
        returns: str: The database connection string.
        """

        # The parentheses around the multi-line string literal allow Python 
        # to automatically concatenate the adjacent string literals into one single string.
        return (
            "Driver={ODBC Driver 17 for SQL Server};"
            f"Server={os.getenv('DB_SERVER', 'localhost')};"
            f"Database={os.getenv('DB_DATABASE', 'N/A')};"
            f"Uid={os.getenv('DB_USERNAME', 'N/A')};"
            f"Pwd={os.getenv('DB_PASSWORD', 'N/A')};"
            "Encrypt=yes;TrustServerCertificate=yes;Connection Timeout=30;"
        )