import os
from datetime import datetime
from fastapi import APIRouter, Response, Request

from services.mysql_test_service import MySQLTestService

router = APIRouter()

#--------------------------------------------------------------------
@router.get("/")
def test_mysql(request: Request, response: Response):
    try:
        # Get query parameters as a dictionary
        query_params = dict(request.query_params)

        MySQLTestService().test()

        data = {
            "app": os.getenv("APP_NAME", "N/A"),
            "version": os.getenv("VERSION", "N/A"),
            "datetime_iso": datetime.now().isoformat()
        }

        response.status_code = 200  # Set the desired HTTP status code
        response.media_type = "application/json"
        return data
    except Exception as e:
        #response.body = json.dumps({"error": str(e)}).encode('utf-8')
        response.status_code = 500  # Set the desired HTTP status code        
        return {"error": str(e)}  