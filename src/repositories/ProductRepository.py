# repository interface / protocol
from typing import Protocol

from models.product_models import ProductModel

class ProductRepository(Protocol):
    def list_products(self) -> list[ProductModel]:
        """List all products."""
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

    def update_product(self, product_id: int, product_data: dict) -> dict:
        """Update an existing product."""
        pass

    def delete_product(self, product_id: int) -> None:
        """
        Delete a product by its ID.

        :param product_id: The ID of the product to delete.
        """
        pass