import os
from datetime import datetime
from fastapi import APIRouter, Response

from models.product_model import ProductModel
from src.services.product_service import ProductService

router = APIRouter()

#--------------------------------------------------------------------
@router.get("/")
async def get_products(response: Response):
    try:
        products : list[ProductModel] = ProductService.get_products()

        data = {
            "app": os.getenv("APP_NAME", "N/A"),
            "version": os.getenv("VERSION", "N/A"),
            "datetime_iso": datetime.now().isoformat(),
            "products": products
        }

        response.status_code = 200  # Set the desired HTTP status code
        response.media_type = "application/json"
        return data
    except Exception as e:
        response.status_code = 500  # Set the desired HTTP status code        
        return {"error": str(e)}          
    finally:
        pass