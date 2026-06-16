import logging
from models.product_models import ProductModel

logger = logging.getLogger(__name__)

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

   #--------------------------------------------------------------------
   def create(self, product: ProductModel) -> int:
      """
      Creates a new product and returns the new product's ID.

      :param:
         product (ProductModel): The product data to insert.

      :return:
         int: The ID of the newly created product.
      """
      try:
         cursor = self.connection.cursor()
         query = """
            INSERT INTO Products 
            (ProductName, ProductDescription, UnitsInStock, SellPrice, DiscountPercentage, UnitsMax) 
            OUTPUT INSERTED.ProductID 
            VALUES (?, ?, ?, ?, ?, ?)
         """
         cursor.execute(
            query,
            (product.ProductName, product.ProductDescription, product.UnitsInStock, 
               product.SellPrice, product.DiscountPercentage, product.UnitsMax)
         )
         row = cursor.fetchone()
         self.connection.commit()
         return row[0] if row else None
      except Exception as e:
         raise e
      finally:
         if cursor:
               cursor.close()               

   #--------------------------------------------------------------------
   def update(self, product: ProductModel) -> int:
      """
      Updates an existing product.

      :param:
         product (ProductModel): The product data to update.

      :return:
         int: The number of rows updated.
      """
      try:
         cursor = self.connection.cursor()
         query = """
            UPDATE Products 
            SET ProductName = ?, ProductDescription = ?, UnitsInStock = ?, 
                  SellPrice = ?, DiscountPercentage = ?, UnitsMax = ? 
            WHERE ProductID = ?
         """ 
         cursor.execute(
               query,
               (product.ProductName, product.ProductDescription, product.UnitsInStock, product.SellPrice, 
               product.DiscountPercentage, product.UnitsMax, product.ProductID)
         )
         self.connection.commit()
         return cursor.rowcount  # Returns the number of rows updated
      except Exception as e:
         raise e
      finally:
         if cursor:
            cursor.close()

   #--------------------------------------------------------------------
   def delete(self, product_id: int) -> int:
      """
      Deletes a product by its ID.

      :param:
         product_id (int): The ID of the product to delete.

      :return:
         int: The number of rows deleted.
      """
      try:
         cursor = self.connection.cursor()

         query = "DELETE FROM Products WHERE ProductID = ?"
         cursor.execute(query, (product_id,))
         self.connection.commit()
         logger.info(f"Deleted product with ID {product_id}, rows affected: {cursor.rowcount}")
         return cursor.rowcount  # Returns the number of rows deleted
      except Exception as e:
         raise e
      finally:
         if cursor:
               cursor.close()