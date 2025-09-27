import os
from datetime import datetime
import json
from fastapi import APIRouter, Response
import pyodbc

from factories.connection_factory import ConnectionFactory
from services.vendor_service import VendorService

router = APIRouter()

#--------------------------------------------------------------------
@router.get("/")
def vendors(response: Response):
    try:
        vendors = VendorService.get_vendors()

        data = {
            "app": os.getenv("APP_NAME", "N/A"),
            "version": os.getenv("VERSION", "N/A"),
            "datetime_iso": datetime.now().isoformat(),
            "vendors": vendors
        }

        response.status_code = 200  # Set the desired HTTP status code
        response.media_type = "application/json"
        #response.body = json.dumps(data).encode('utf-8')
        return data
    except Exception as e:
        #response.body = json.dumps({"error": str(e)}).encode('utf-8')
        response.status_code = 500  # Set the desired HTTP status code        
        return {"error": str(e)}          
    finally:
        pass

#--------------------------------------------------------------------
@router.get("/{vendor_id}")
def get_vendor(vendor_id: int, response: Response):
    try:
        vendor = VendorService.get_vendor_by_id(vendor_id)
        if vendor:
            response.status_code = 200
            return vendor
        else:
            response.status_code = 404
            return {"error": "Vendor not found"}
    except Exception as e:
        response.status_code = 500
        return {"error": str(e)}
    finally:
        pass