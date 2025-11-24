from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class VendorModel(BaseModel):
    VendorID: Optional[int] = Field(None, description="Primary key, auto-incremented")
    VendorName: str = Field(..., max_length=50)
    VendorPhone: str = Field(..., max_length=10)
    Email: Optional[str] = Field(None, max_length=50)