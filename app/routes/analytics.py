from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.db import get_db
from app.models.order import Order, OrderItem
from app.models.product import Inventory
from app.schemas.analytics import (
    AnalyticsSummaryResponse,
    TopProductsResponse,
    TopProductItem,
)

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/summary", response_model=AnalyticsSummaryResponse)
def get_summary(range: str = Query("monthly"), db: Session = Depends(get_db)):
    total_sales = db.query(func.coalesce(func.sum(Order.total_amount), 0)).scalar() or 0
    order_count = db.query(func.count(Order.id)).scalar() or 0

    total_units_sold = db.query(func.coalesce(func.sum(OrderItem.quantity), 0)).scalar() or 0
    total_stock = db.query(func.coalesce(func.sum(Inventory.stock_quantity), 0)).scalar() or 0

    inventory_turnover = float(total_units_sold / total_stock) if total_stock > 0 else 0.0

    return {
        "total_sales": float(total_sales),
        "order_count": int(order_count),
        "inventory_turnover": inventory_turnover
    }


@router.get("/top-products", response_model=TopProductsResponse)
def get_top_products(range: str = Query("monthly"), db: Session = Depends(get_db)):
    rows = (
        db.query(
            OrderItem.product_id,
            func.coalesce(func.sum(OrderItem.quantity), 0).label("units_sold"),
            func.coalesce(func.sum(OrderItem.quantity * OrderItem.unit_price), 0).label("revenue")
        )
        .group_by(OrderItem.product_id)
        .order_by(func.sum(OrderItem.quantity).desc())
        .limit(5)
        .all()
    )

    return {
        "items": [
            TopProductItem(
                product_id=row.product_id,
                units_sold=int(row.units_sold),
                revenue=float(row.revenue)
            )
            for row in rows
        ]
    }