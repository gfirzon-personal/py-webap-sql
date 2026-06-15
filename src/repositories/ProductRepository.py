# repository interface / protocol
from typing import Protocol

from models.product_models import ProductModel

class ProductRepository(Protocol):
    def list_products(self) -> list[ProductModel]:
        """List all products."""
        pass

    def get_product_by_id(self, product_id: int) -> ProductModel | None:
        """Fetch a product by its ID."""
        pass

    def create_product(self, product_data: dict) -> dict:
        """Create a new product."""
        pass

    def update_product(self, product_id: int, product_data: dict) -> dict:
        """Update an existing product."""
        pass

    def delete_product(self, product_id: int) -> None:
        """Delete a product by its ID."""
        pass