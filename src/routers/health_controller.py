import os
import logging
from datetime import datetime
from fastapi import APIRouter, Response, status, Depends
import pyodbc
from common.config import Settings, get_settings

router = APIRouter()

logger = logging.getLogger(__name__)

#--------------------------------------------------------------------
@router.get("")
def health(response: Response):
    try:
        data = {
            "app": os.getenv("APP_NAME", "N/A"),
            "version": os.getenv("VERSION", "N/A"),
            "datetime_iso": datetime.now().isoformat()
        }

        print(pyodbc.drivers())

        response.status_code = status.HTTP_200_OK  # Set the desired HTTP status code
        response.media_type = "application/json"
        #response.body = json.dumps(data).encode('utf-8')
        return data
    except Exception as e:
        #response.body = json.dumps({"error": str(e)}).encode('utf-8')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR  # Set the desired HTTP status code
        return {"error": str(e)}   

#--------------------------------------------------------------------
@router.get("/info")
async def get_app_info(settings: Settings = Depends(get_settings)):
    try:
        return settings
    except Exception as e:
        logger.error(f"Error fetching app info: {str(e)}")
        return {"error": str(e)}

