import os

class ConnectionFactory:

    @staticmethod
    def get_connection():
        import pyodbc
        return pyodbc.connect(ConnectionFactory.get_connection_string())

    @staticmethod
    def get_connection_string():
        return (
            "Driver={ODBC Driver 17 for SQL Server};"
            f"Server={os.getenv('DB_SERVER', 'localhost')};"
            f"Database={os.getenv('DB_DATABASE', 'N/A')};"
            f"Uid={os.getenv('DB_USERNAME', 'N/A')};"
            f"Pwd={os.getenv('DB_PASSWORD', 'N/A')};"
            "Encrypt=yes;TrustServerCertificate=yes;Connection Timeout=30;"
        )