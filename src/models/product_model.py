from pydantic import BaseModel, Field
from typing import Optional

class ProductModel(BaseModel):
    ProductID: Optional[int] = Field(None, description="Primary key, auto-incremented")
    ProductName: str = Field(..., max_length=50)
    ProductDescription: Optional[str] = Field(None, max_length=250)
    UnitsInStock: int
    SellPrice: float  # 'money' type maps to float/Decimal in Python
    DiscountPercentage: Optional[int] = None
    UnitsMax: int