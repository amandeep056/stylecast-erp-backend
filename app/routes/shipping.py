from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.shipping import ShippingRule
from app.models.brand import Brand
from app.schemas.shipping import (
    ShippingRuleCreate,
    ShippingRuleUpdate,
    ShippingRuleResponse,
)

router = APIRouter(prefix="/shipping-rules", tags=["Shipping Rules"])


@router.post("/", response_model=ShippingRuleResponse)
def create_shipping_rule(rule: ShippingRuleCreate, db: Session = Depends(get_db)):
    brand = db.query(Brand).filter(Brand.id == rule.brand_id).first()
    if not brand:
        raise HTTPException(status_code=404, detail="Brand not found")

    new_rule = ShippingRule(
        brand_id=rule.brand_id,
        region=rule.region,
        shipping_fee=rule.shipping_fee,
        free_shipping_threshold=rule.free_shipping_threshold,
        delivery_estimate_days=rule.delivery_estimate_days,
    )

    db.add(new_rule)
    db.commit()
    db.refresh(new_rule)
    return new_rule


@router.get("/", response_model=list[ShippingRuleResponse])
def list_shipping_rules(db: Session = Depends(get_db)):
    return db.query(ShippingRule).all()


@router.get("/{rule_id}", response_model=ShippingRuleResponse)
def get_shipping_rule(rule_id: int, db: Session = Depends(get_db)):
    rule = db.query(ShippingRule).filter(ShippingRule.id == rule_id).first()
    if not rule:
        raise HTTPException(status_code=404, detail="Shipping rule not found")
    return rule


@router.put("/{rule_id}", response_model=ShippingRuleResponse)
def update_shipping_rule(rule_id: int, rule_update: ShippingRuleUpdate, db: Session = Depends(get_db)):
    rule = db.query(ShippingRule).filter(ShippingRule.id == rule_id).first()
    if not rule:
        raise HTTPException(status_code=404, detail="Shipping rule not found")

    update_data = rule_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(rule, key, value)

    db.commit()
    db.refresh(rule)
    return rule


@router.delete("/{rule_id}")
def delete_shipping_rule(rule_id: int, db: Session = Depends(get_db)):
    rule = db.query(ShippingRule).filter(ShippingRule.id == rule_id).first()
    if not rule:
        raise HTTPException(status_code=404, detail="Shipping rule not found")

    db.delete(rule)
    db.commit()
    return {"message": "Shipping rule deleted successfully"}