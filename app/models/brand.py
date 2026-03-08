from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db import Base

class Brand(Base):
    __tablename__ = "brands"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    company_info = Column(String(500), nullable=True)
    website = Column(String(255), nullable=True)
    shipping_origin = Column(String(255), nullable=True)
    category = Column(String(100), nullable=True)
    contact_email = Column(String(255), nullable=False, unique=True)
    is_approved = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    users = relationship("User", back_populates="brand", cascade="all, delete")
    products = relationship("Product", back_populates="brand", cascade="all, delete")
    orders = relationship("Order", back_populates="brand", cascade="all, delete")
    shipping_rules = relationship("ShippingRule", back_populates="brand", cascade="all, delete")