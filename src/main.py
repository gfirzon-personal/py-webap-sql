import os
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from common.pretty_json_response import PrettyJSONResponse
from common.screen_utils import clear_console
from routers import (health_controller, greetings_controller, vendors_controller, favicon_controller)

load_dotenv()  # take environment variables from .env.

app = FastAPI(
    title = os.getenv("APP_NAME", "N/A"),
    description = os.getenv("APP_DESCRIPTION", "N/A"),
    version = os.getenv("VERSION", "N/A"),
    default_response_class=PrettyJSONResponse
    )

# Configure CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)    

# Add favicon endpoint to suppress 404 errors
@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return Response(status_code=204)

app.include_router(health_controller.router, prefix="/health", tags=["health"])
app.include_router(greetings_controller.router, prefix="/greetings", tags=["greetings"])
app.include_router(vendors_controller.router, prefix="/vendors", tags=["vendors"])
app.include_router(favicon_controller.router, prefix="/favicon", tags=["favicon"])

clear_console()


