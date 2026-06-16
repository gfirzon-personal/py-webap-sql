# repository interface / protocol
from typing import Protocol

from models.product_models import ProductModel

class ProductRepository(Protocol):
    def list_products(self) -> list[ProductModel]:
        """
        List all products.
        :return: A list of ProductModel instances."""
        pass

    def get_product_by_id(self, product_id: int) -> ProductModel | None:
        """
        Fetch a product by its ID.

        :param product_id: The ID of the product to fetch.
        :return: The product if found, otherwise None.
        """
        pass

    def create(self, product: ProductModel) -> int:
        """
        Create a new product.

        :param product: The product to create.
        :return: The ID of the created product."""
        pass

    def update(self, product: ProductModel) -> int:
        """
        Update an existing product.

        :param product: The product data to update.
        :return: The number of rows updated.
        """
        pass

    def delete_product(self, product_id: int) -> int:
        """
        Delete a product by its ID.

        :param product_id: The ID of the product to delete.
        :return: The number of rows deleted.
        """
        pass