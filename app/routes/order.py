from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.order import Order, OrderItem
from app.models.product import ProductVariant, Inventory
from app.schemas.order import OrderCreate, OrderResponse, OrderStatusUpdate

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    total = 0
    created_items = []

    for item in order.items:
        variant = db.query(ProductVariant).filter(ProductVariant.id == item.variant_id).first()
        if not variant:
            raise HTTPException(status_code=404, detail=f"Variant {item.variant_id} not found")

        inventory = db.query(Inventory).filter(Inventory.variant_id == item.variant_id).first()
        if not inventory:
            raise HTTPException(status_code=404, detail=f"Inventory missing for variant {item.variant_id}")

        if inventory.stock_quantity < item.quantity:
            raise HTTPException(status_code=400, detail=f"Insufficient stock for variant {item.variant_id}")

        inventory.stock_quantity -= item.quantity
        total += item.quantity * item.unit_price
        created_items.append(item)

    new_order = Order(
        brand_id=order.brand_id,
        customer_name=order.customer_name,
        customer_email=order.customer_email,
        country=order.country,
        city=order.city,
        postal_code=order.postal_code,
        payment_status="pending",
        order_status="pending",
        total_amount=total
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    for item in created_items:
        db_item = OrderItem(
            order_id=new_order.id,
            product_id=item.product_id,
            variant_id=item.variant_id,
            quantity=item.quantity,
            unit_price=item.unit_price
        )
        db.add(db_item)

    db.commit()
    db.refresh(new_order)
    return new_order


@router.get("/", response_model=list[OrderResponse])
def list_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()


@router.get("/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.put("/{order_id}/status", response_model=OrderResponse)
def update_order_status(order_id: int, status_update: OrderStatusUpdate, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order.order_status = status_update.order_status
    db.commit()
    db.refresh(order)
    return order