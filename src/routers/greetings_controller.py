import os
from datetime import datetime
import json
from fastapi import APIRouter, Response, Request
import pyodbc

router = APIRouter()

#--------------------------------------------------------------------
@router.get("/")
def greetings(request: Request, response: Response):
    try:
        # Get query parameters as a dictionary
        query_params = dict(request.query_params)

        data = {
            "app": os.getenv("APP_NAME", "N/A"),
            "version": os.getenv("VERSION", "N/A"),
            "datetime_iso": datetime.now().isoformat(),
            "data": f"Hello, {query_params.get('name', 'unknown person :)')}!",
        }

        response.status_code = 200  # Set the desired HTTP status code
        response.media_type = "application/json"
        #response.body = json.dumps(data).encode('utf-8')
        return data
    except Exception as e:
        #response.body = json.dumps({"error": str(e)}).encode('utf-8')
        response.status_code = 500  # Set the desired HTTP status code        
        return {"error": str(e)}          

