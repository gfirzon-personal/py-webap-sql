import os
import logging
from factories.connection_factory import ConnectionFactory
from models.product_models import ProductModel

logger = logging.getLogger(__name__)

class ProductService:
    #--------------------------------------------------------------------
    @staticmethod
    def get_products() -> list[ProductModel]:
        """
        Retrieves a list of all products.

        :return:
            list[ProductModel]: A list of product objects.
        """
        conn = None
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

    #--------------------------------------------------------------------
    @staticmethod
    def get_product(product_id: int) -> ProductModel | None:
        """
        Retrieves a product by its ID.

        :param:
            product_id (int): The ID of the product to retrieve.

        :return:
            ProductModel | None: The product object if found, otherwise None.
        """
        conn = None
        try:
            conn = ConnectionFactory.get_connection()
            cursor = conn.cursor()
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
            if conn:
                conn.close()   

    #--------------------------------------------------------------------
    @staticmethod
    def create(product: ProductModel) -> int:
        """
        Creates a new product and returns the new product's ID.

        :param:
            product (ProductModel): The product data to insert.

        :return:
            int: The ID of the newly created product.
        """
        conn = None
        try:
            conn = ConnectionFactory.get_connection()
            cursor = conn.cursor()
            query = """
                INSERT INTO Products (ProductName, ProductDescription, UnitsInStock, SellPrice, DiscountPercentage, UnitsMax) 
                OUTPUT INSERTED.ProductID 
                VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(
                query,
                (product.ProductName, product.ProductDescription, product.UnitsInStock, product.SellPrice, product.DiscountPercentage, product.UnitsMax)
            )
            row = cursor.fetchone()
            conn.commit()
            return row[0] if row else None
        except Exception as e:
            raise e
        finally:
            if conn:
                conn.close()        

    #--------------------------------------------------------------------
    @staticmethod
    def update(product: ProductModel) -> int:
        """
        Updates an existing product.

        :param:
            product (ProductModel): The product data to update.

        :return:
            int: The number of rows updated.
        """
        conn = None
        try:
            conn = ConnectionFactory.get_connection()
            cursor = conn.cursor()
            query = """
                UPDATE Products 
                SET ProductName = ?, ProductDescription = ?, UnitsInStock = ?, SellPrice = ?, DiscountPercentage = ?, UnitsMax = ? 
                WHERE ProductID = ?
            """ 
            cursor.execute(
                query,
                (product.ProductName, product.ProductDescription, product.UnitsInStock, product.SellPrice, 
                 product.DiscountPercentage, product.UnitsMax, product.ProductID)
            )
            conn.commit()
            return cursor.rowcount  # Returns the number of rows updated
        except Exception as e:
            raise e
        finally:
            if conn:
                conn.close()            

    #--------------------------------------------------------------------
    @staticmethod
    def delete(id: int) -> int:
        """
        Deletes a product by its ID.

        :param:
            id (int): The ID of the product to delete.

        :return:
            int: The number of rows deleted.
        """
        conn = None
        try:
            conn = ConnectionFactory.get_connection()
            cursor = conn.cursor()
            query = "DELETE FROM Products WHERE ProductID = ?"
            cursor.execute(query, (id,))
            conn.commit()
            return cursor.rowcount  # Returns the number of rows deleted
        except Exception as e:
            raise e
        finally:
            if conn:
                conn.close()                                         