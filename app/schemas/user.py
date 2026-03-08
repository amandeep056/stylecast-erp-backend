from pydantic import BaseModel, EmailStr
from typing import Optional


class UserRegister(BaseModel):
    brand_id: int
    name: str
    email: EmailStr
    password: str
    role: Optional[str] = "Brand Owner"


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    brand_id: int
    name: str
    email: EmailStr
    role: str

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    token_type: str