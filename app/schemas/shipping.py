from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ShippingRuleCreate(BaseModel):
    brand_id: int
    region: str
    shipping_fee: float
    free_shipping_threshold: Optional[float] = None
    delivery_estimate_days: Optional[int] = None


class ShippingRuleUpdate(BaseModel):
    region: Optional[str] = None
    shipping_fee: Optional[float] = None
    free_shipping_threshold: Optional[float] = None
    delivery_estimate_days: Optional[int] = None


class ShippingRuleResponse(BaseModel):
    id: int
    brand_id: int
    region: str
    shipping_fee: float
    free_shipping_threshold: Optional[float] = None
    delivery_estimate_days: Optional[int] = None
    created_at: datetime

    class Config:
        from_attributes = True