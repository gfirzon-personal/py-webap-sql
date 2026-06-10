import os
import logging
from datetime import datetime
from fastapi import APIRouter, Response, status

from models.product_models import ProductModel, ProductResponseModel, ProductsResponseModel
from src.services.product_service import ProductService

router = APIRouter()
logger = logging.getLogger(__name__)

#--------------------------------------------------------------------
@router.get("")
async def get_products(response: Response):
    try:
        products : list[ProductModel] = ProductService.get_products()

        data = {
            "app": os.getenv("APP_NAME", "N/A"),
            "version": os.getenv("VERSION", "N/A"),
            "datetime_iso": datetime.now().isoformat(),
            "products": products
        }

        response.status_code = status.HTTP_200_OK  # Set the desired HTTP status code
        response.media_type = "application/json"
        return data
    except Exception as e:
        response.status_code = 500  # Set the desired HTTP status code        
        return {"error": str(e)}          
    finally:
        pass

#--------------------------------------------------------------------
@router.get("/{id}", response_model=ProductResponseModel)
def get_product(id: int, response: Response):
    try:
        product = ProductService.get_product(id)
        data : dict = {
            "app": os.getenv("APP_NAME", "N/A"),
            "version": os.getenv("VERSION", "N/A"),
            "datetime_iso": datetime.now().isoformat(),
        }        

        if product:
            response.status_code = status.HTTP_200_OK
            data["product"] = product
            return ProductResponseModel(**data)
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
            data["error"] = "Product not found"            
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        data["error"] = str(e)     

#--------------------------------------------------------------------
@router.post("")
def create(product: ProductModel, response: Response):
    try:
        product_id = ProductService.create(product)
        response.status_code = status.HTTP_201_CREATED
        return {"id": product_id}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    finally:
        pass        