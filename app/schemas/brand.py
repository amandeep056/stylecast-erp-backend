from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class BrandCreate(BaseModel):
    name: str
    company_info: Optional[str] = None
    website: Optional[str] = None
    shipping_origin: Optional[str] = None
    category: Optional[str] = None
    contact_email: EmailStr


class BrandResponse(BaseModel):
    id: int
    name: str
    company_info: Optional[str] = None
    website: Optional[str] = None
    shipping_origin: Optional[str] = None
    category: Optional[str] = None
    contact_email: EmailStr
    is_approved: bool
    created_at: datetime

    class Config:
        from_attributes = True