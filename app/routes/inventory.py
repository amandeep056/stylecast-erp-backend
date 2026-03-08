from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.product import ProductVariant, Inventory
from app.schemas.inventory import InventoryCreate, InventoryUpdate, InventoryResponse

router = APIRouter(prefix="/inventory", tags=["Inventory"])


@router.post("/", response_model=InventoryResponse)
def create_inventory(inventory: InventoryCreate, db: Session = Depends(get_db)):
    variant = db.query(ProductVariant).filter(ProductVariant.id == inventory.variant_id).first()
    if not variant:
        raise HTTPException(status_code=404, detail="Variant not found")

    existing_inventory = db.query(Inventory).filter(Inventory.variant_id == inventory.variant_id).first()
    if existing_inventory:
        raise HTTPException(status_code=400, detail="Inventory already exists for this variant")

    new_inventory = Inventory(
        brand_id=inventory.brand_id,
        variant_id=inventory.variant_id,
        stock_quantity=inventory.stock_quantity,
        low_stock_threshold=inventory.low_stock_threshold
    )

    db.add(new_inventory)
    db.commit()
    db.refresh(new_inventory)
    return new_inventory


@router.get("/", response_model=list[InventoryResponse])
def list_inventory(db: Session = Depends(get_db)):
    return db.query(Inventory).all()


@router.put("/{variant_id}", response_model=InventoryResponse)
def update_inventory(variant_id: int, inventory_update: InventoryUpdate, db: Session = Depends(get_db)):
    inventory = db.query(Inventory).filter(Inventory.variant_id == variant_id).first()
    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory record not found")

    inventory.stock_quantity = inventory_update.stock_quantity
    inventory.low_stock_threshold = inventory_update.low_stock_threshold

    db.commit()
    db.refresh(inventory)
    return inventory