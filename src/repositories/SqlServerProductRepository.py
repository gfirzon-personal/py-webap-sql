from models.product_models import ProductModel
from src.factories.connection_factory import ConnectionFactory

class SqlServerProductRepository:
   def __init__(self, connection):
      self.connection = connection

   #--------------------------------------------------------------------
   def list_products(self) -> list[ProductModel]:
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

   #--------------------------------------------------------------------
   def get_product_by_id(self, product_id) -> ProductModel | None:
      try:
         cursor = self.connection.cursor()

         query = "SELECT * FROM Products WHERE ProductID = ?"
         cursor.execute(query, (product_id,))  # Adjust the query as needed
         row = cursor.fetchone()
         if row:
            # The ** is Python's dictionary unpacking operator.
            return ProductModel(**dict(zip([column[0] for column in cursor.description], row)))
         else:
            return None
      except Exception as e:
         raise e
      finally:
         if cursor:
               cursor.close()