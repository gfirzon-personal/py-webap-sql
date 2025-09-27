from factories.connection_factory import ConnectionFactory


class VendorService:
    @staticmethod
    def get_vendors():
        try:
            conn = ConnectionFactory.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Vendors")  # Adjust the query as needed
            rows = cursor.fetchall()
            return [dict(zip([column[0] for column in cursor.description], row)) for row in rows]
        except Exception as e:
            raise e
        finally:
            if conn:
                conn.close()