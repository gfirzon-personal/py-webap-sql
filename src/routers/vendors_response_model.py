from pydantic import BaseModel
from typing import List, Optional

from models.vendor_model import VendorModel

class VendorsResponseModel(BaseModel):
    app: str
    version: str
    datetime_iso: str
    vendors: List[VendorModel]

class VendorResponseModel(BaseModel):
    app: str
    version: str
    datetime_iso: str
    vendor: Optional[VendorModel] = None
    error: Optional[str] = None
