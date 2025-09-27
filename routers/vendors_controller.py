import os
from datetime import datetime
import json
from fastapi import APIRouter, Response
import pyodbc

from factories.connection_factory import ConnectionFactory

router = APIRouter()

#--------------------------------------------------------------------
@router.get("/")
def vendors(response: Response):
    try:
        conn = ConnectionFactory.get_connection()

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Vendors")  # Adjust the query as needed
        rows = cursor.fetchall()

        data = {
            "app": os.getenv("APP_NAME", "N/A"),
            "version": os.getenv("VERSION", "N/A"),
            "datetime_iso": datetime.now().isoformat(),
            "vendors": [dict(zip([column[0] for column in cursor.description], row)) for row in rows]
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
        if conn:
            conn.close()
