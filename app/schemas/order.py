from pydantic import BaseModel, EmailStr
from typing import List
from datetime import datetime


class OrderItemCreate(BaseModel):
    product_id: int | None = None
    variant_id: int
    quantity: int
    unit_price: float


class OrderCreate(BaseModel):
    brand_id: int
    customer_name: str
    customer_email: EmailStr
    country: str
    city: str
    postal_code: str
    items: List[OrderItemCreate]


class OrderStatusUpdate(BaseModel):
    order_status: str


class OrderItemResponse(BaseModel):
    id: int
    product_id: int | None = None
    variant_id: int | None = None
    quantity: int
    unit_price: float

    class Config:
        from_attributes = True


class OrderResponse(BaseModel):
    id: int
    brand_id: int
    customer_name: str
    customer_email: EmailStr
    country: str
    city: str
    postal_code: str
    payment_status: str
    order_status: str
    total_amount: float
    created_at: datetime
    items: List[OrderItemResponse]

    class Config:
        from_attributes = True