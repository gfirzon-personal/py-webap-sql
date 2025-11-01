from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class VendorModel(BaseModel):
    VendorID: int = 0 # Default to 0 for new vendors
    VendorName: str
    VendorPhone: str
    Email: str