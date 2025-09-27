import os
from datetime import datetime
import json
from fastapi import APIRouter, Response

router = APIRouter()

#--------------------------------------------------------------------
@router.get("/")
def health(response: Response):
    try:
        data = {
            "app": os.getenv("APP_NAME", "N/A"),
            "version": os.getenv("VERSION", "N/A"),
            "datetime_iso": datetime.now().isoformat()
        }

        response.status_code = 200  # Set the desired HTTP status code
        response.media_type = "application/json"
        #response.body = json.dumps(data).encode('utf-8')
        return data
    except Exception as e:
        #response.body = json.dumps({"error": str(e)}).encode('utf-8')
        response.status_code = 500  # Set the desired HTTP status code        
        return {"error": str(e)}          

