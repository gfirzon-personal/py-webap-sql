import os
import logging
from factories.connection_factory import ConnectionFactory
from models.product_models import ProductModel
from repositories import ProductRepository

logger = logging.getLogger(__name__)

class ProductService:
   def __init__(self, repo: ProductRepository):
      self.repo = repo    

   def list_products(self) -> list[ProductModel]:
      return self.repo.list_products()