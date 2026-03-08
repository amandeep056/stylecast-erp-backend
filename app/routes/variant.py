from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.product import Product, ProductVariant
from app.schemas.variant import VariantCreate, VariantResponse

router = APIRouter(prefix="/variants", tags=["Variants"])


@router.post("/", response_model=VariantResponse)
def create_variant(variant: VariantCreate, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == variant.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    existing_sku = db.query(ProductVariant).filter(ProductVariant.sku == variant.sku).first()
    if existing_sku:
        raise HTTPException(status_code=400, detail="SKU already exists")

    new_variant = ProductVariant(
        brand_id=variant.brand_id,
        product_id=variant.product_id,
        size=variant.size,
        color=variant.color,
        material=variant.material,
        sku=variant.sku,
        price_override=variant.price_override
    )

    db.add(new_variant)
    db.commit()
    db.refresh(new_variant)
    return new_variant


@router.get("/", response_model=list[VariantResponse])
def list_variants(db: Session = Depends(get_db)):
    return db.query(ProductVariant).all()