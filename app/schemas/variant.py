from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class VariantCreate(BaseModel):
    brand_id: int
    product_id: int
    size: Optional[str] = None
    color: Optional[str] = None
    material: Optional[str] = None
    sku: str
    price_override: Optional[float] = None


class VariantResponse(BaseModel):
    id: int
    brand_id: int
    product_id: int
    size: Optional[str] = None
    color: Optional[str] = None
    material: Optional[str] = None
    sku: str
    price_override: Optional[float] = None
    created_at: datetime

    class Config:
        from_attributes = True