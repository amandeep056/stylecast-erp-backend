from pydantic import BaseModel
from typing import List, Optional


class AnalyticsSummaryResponse(BaseModel):
    total_sales: float
    order_count: int
    inventory_turnover: float


class TopProductItem(BaseModel):
    product_id: Optional[int] = None
    units_sold: int
    revenue: float


class TopProductsResponse(BaseModel):
    items: List[TopProductItem]