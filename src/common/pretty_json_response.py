from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json

class PrettyJSONResponse(JSONResponse):
    def render(self, content: any) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=4  # Pretty print with 4 spaces
        ).encode("utf-8")

# app = FastAPI(default_response_class=PrettyJSONResponse)

# ...existing code...