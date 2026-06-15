from models.product_models import ProductModel

class SqlServerProductRepository:
    def __init__(self, connection):
        self.connection = connection

    def list_products(self) -> list:
      try:
          cursor = self.connection.cursor()
          query = "SELECT * FROM Products"
          cursor.execute(query)  
          rows = cursor.fetchall()
          return [ProductModel(**dict(zip([column[0] for column in cursor.description], row))) for row in rows]
      except Exception as e:
          raise e
      finally:
          cursor.close()

    def get_product_by_id(self, product_id):
        cursor = self.connection.cursor()
        query = "SELECT * FROM Products WHERE ProductID = ?"
        cursor.execute(query, (product_id,))
        result = cursor.fetchone()
        cursor.close()
        return result