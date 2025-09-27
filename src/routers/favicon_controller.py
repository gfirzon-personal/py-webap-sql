from fastapi import APIRouter, Response
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/favicon.ico")
def favicon():
    return FileResponse("Favicon.ico.png")