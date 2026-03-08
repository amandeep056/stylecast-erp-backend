from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.brand import Brand
from app.schemas.brand import BrandCreate, BrandResponse

router = APIRouter(prefix="/brands", tags=["Brands"])


@router.post("/", response_model=BrandResponse)
def create_brand(brand: BrandCreate, db: Session = Depends(get_db)):
    existing_brand = db.query(Brand).filter(
        (Brand.name == brand.name) | (Brand.contact_email == brand.contact_email)
    ).first()

    if existing_brand:
        raise HTTPException(status_code=400, detail="Brand name or contact email already exists")

    new_brand = Brand(
        name=brand.name,
        company_info=brand.company_info,
        website=brand.website,
        shipping_origin=brand.shipping_origin,
        category=brand.category,
        contact_email=brand.contact_email,
        is_approved=True
    )

    db.add(new_brand)
    db.commit()
    db.refresh(new_brand)

    return new_brand


@router.get("/", response_model=list[BrandResponse])
def list_brands(db: Session = Depends(get_db)):
    return db.query(Brand).all()