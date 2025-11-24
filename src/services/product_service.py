from factories.connection_factory import ConnectionFactory
from src.models.product_model import ProductModel

class ProductService:
    #--------------------------------------------------------------------
    @staticmethod
    def get_products() -> list[ProductModel]:
        """
        Retrieves a list of all products.

        :return:
            list[ProductModel]: A list of product objects.
        """
        try:
            conn = ConnectionFactory.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Products")  # Adjust the query as needed
            rows = cursor.fetchall()
            return [ProductModel(**dict(zip([column[0] for column in cursor.description], row))) for row in rows]
        except Exception as e:
            raise e
        finally:
            if conn:
                conn.close()