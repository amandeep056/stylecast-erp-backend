from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db import Base


class ShippingRule(Base):
    __tablename__ = "shipping_rules"

    id = Column(Integer, primary_key=True, index=True)
    brand_id = Column(Integer, ForeignKey("brands.id", ondelete="CASCADE"), nullable=False, index=True)
    region = Column(String(100), nullable=False)
    shipping_fee = Column(Numeric(10, 2), nullable=False)
    free_shipping_threshold = Column(Numeric(10, 2), nullable=True)
    delivery_estimate_days = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    brand = relationship("Brand", back_populates="shipping_rules")