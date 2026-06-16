import os
import logging
from datetime import datetime
from fastapi import APIRouter, Depends, Response, status

from models.product_models import ProductModel, ProductResponseModel, ProductsResponseModel
from services.product_service import ProductService
from factories.product_repository_factory import ProductRepositoryFactory

router = APIRouter()
logger = logging.getLogger(__name__)

def get_product_service() -> ProductService:
    repo = ProductRepositoryFactory.create()
    return ProductService(repo)

#--------------------------------------------------------------------
@router.get("")
async def get_products(
    response: Response,
    service: ProductService = Depends(get_product_service)
    ):
    try:
        products : list[ProductModel] = service.list_products()

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
def get_product(
        id: int, 
        response: Response,
        service: ProductService = Depends(get_product_service)
    ):
    try:
        product = service.get_product(id)
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
def create(
    product: ProductModel, 
    response: Response,
    service: ProductService = Depends(get_product_service)
    ):
    try:
        product_id = service.create(product)
        response.status_code = status.HTTP_201_CREATED
        return {"id": product_id}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    finally:
        pass        

#--------------------------------------------------------------------
@router.put("")
def update(product: ProductModel, response: Response):
    try:
        rows_updated = get_product_service().update(product)
        if rows_updated > 0:
            response.status_code = status.HTTP_200_OK
            return {"message": "Product updated successfully"}
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"error": "Product not found"}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    finally:
        pass 

#--------------------------------------------------------------------
@router.delete("/{id}")
def delete(id: int, response: Response):
    try:
        rows_deleted = get_product_service().delete(id)
        if rows_deleted > 0:
            response.status_code = status.HTTP_200_OK
            return {"message": "Product deleted successfully"}
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"error": "Product not found"}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    finally:
        pass