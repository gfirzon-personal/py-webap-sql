import os
from datetime import datetime
from fastapi import APIRouter, Response, status

from services.vendor_service import VendorService
from models.vendor_model import VendorModel
from routers.vendors_response_model import VendorResponseModel

router = APIRouter()

#--------------------------------------------------------------------
@router.get("") # Note: Changed from "/" to "" to avoid conflict with other routes
def vendors(response: Response):
    try:
        vendors : list[VendorModel] = VendorService.get_vendors()

        data = {
            "app": os.getenv("APP_NAME", "N/A"),
            "version": os.getenv("VERSION", "N/A"),
            "datetime_iso": datetime.now().isoformat(),
            "vendors": vendors
        }

        response.status_code = status.HTTP_200_OK  # Set the desired HTTP status code
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
@router.get("/{vendor_id}", response_model=VendorResponseModel)
def get_vendor(vendor_id: int, response: Response):
    try:
        vendor = VendorService.get_vendor_by_id(vendor_id)
        data : dict = {
            "app": os.getenv("APP_NAME", "N/A"),
            "version": os.getenv("VERSION", "N/A"),
            "datetime_iso": datetime.now().isoformat(),
        }        

        if vendor:
            response.status_code = status.HTTP_200_OK
            data["vendor"] = vendor
            return VendorResponseModel(**data)
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
            data["error"] = "Vendor not found"            
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        data["error"] = str(e)
    finally:
        return VendorResponseModel(**data)        

#--------------------------------------------------------------------
@router.post("/")
def create_vendor(vendor: VendorModel, response: Response):
    try:
        vendor_id = VendorService.create_vendor(vendor)
        response.status_code = status.HTTP_201_CREATED
        return {"id": vendor_id}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    finally:
        pass

#--------------------------------------------------------------------
@router.put("/")
def update_vendor(vendor: VendorModel, response: Response):
    try:
        rows_updated = VendorService.update_vendor(vendor)
        if rows_updated > 0:
            response.status_code = status.HTTP_200_OK
            return {"message": "Vendor updated successfully"}
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"error": "Vendor not found"}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    finally:
        pass

#--------------------------------------------------------------------
@router.delete("/{vendor_id}")
def delete_vendor(vendor_id: int, response: Response):
    try:
        rows_deleted = VendorService.delete_vendor(vendor_id)
        if rows_deleted > 0:
            response.status_code = status.HTTP_200_OK
            return {"message": "Vendor deleted successfully"}
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"error": "Vendor not found"}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    finally:
        pass