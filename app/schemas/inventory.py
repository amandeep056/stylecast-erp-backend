from pydantic import BaseModel
from datetime import datetime


class InventoryCreate(BaseModel):
    brand_id: int
    variant_id: int
    stock_quantity: int
    low_stock_threshold: int = 5


class InventoryUpdate(BaseModel):
    stock_quantity: int
    low_stock_threshold: int = 5


class InventoryResponse(BaseModel):
    id: int
    brand_id: int
    variant_id: int
    stock_quantity: int
    low_stock_threshold: int
    updated_at: datetime

    class Config:
        from_attributes = True