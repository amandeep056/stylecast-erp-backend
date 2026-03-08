from fastapi import FastAPI
from app.db import Base, engine
from app.models import Brand, User, Product, ProductVariant, Inventory, Order, OrderItem, ShippingRule
from app.routes.brand import router as brand_router
from app.routes.auth import router as auth_router
from app.routes.product import router as product_router
from app.routes.variant import router as variant_router
from app.routes.inventory import router as inventory_router
from app.routes.order import router as order_router
from app.routes.shipping import router as shipping_router
from app.routes.analytics import router as analytics_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="StyleCast ERP Backend")

app.include_router(brand_router)
app.include_router(auth_router)
app.include_router(product_router)
app.include_router(variant_router)
app.include_router(inventory_router)
app.include_router(order_router)
app.include_router(shipping_router)
app.include_router(analytics_router)
@app.get("/")
def root():
    return {"message": "StyleCast ERP backend running"}