from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProductCreate(BaseModel):
    brand_id: int
    title: str
    description: Optional[str] = None
    category: Optional[str] = None
    base_price: float
    status: Optional[str] = "active"


class ProductUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    base_price: Optional[float] = None
    status: Optional[str] = None


class ProductResponse(BaseModel):
    id: int
    brand_id: int
    title: str
    description: Optional[str] = None
    category: Optional[str] = None
    base_price: float
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True