from datetime import datetime, timezone
from typing import Optional
from uuid import uuid4

from fastapi import FastAPI, Header
from pydantic import BaseModel, Field

app = FastAPI(
    title="E&M Shop Sales Service",
    version="1.0.0",
    description="Multi-tenant UGX shop sales microservice (SDAF v1.0 Live Demo).",
)

SALES_STORE: list[dict] = []


class SaleCreateRequest(BaseModel):
    tenant_id: str = Field(..., min_length=1, description="Shop tenant identifier")
    item_sku: str = Field(..., min_length=1, description="Product SKU code")
    quantity: int = Field(..., gt=0, description="Number of units sold")
    unit_price_ugx: float = Field(..., gt=0, description="Unit price in UGX")


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@app.post("/sales", status_code=201)
def record_sale(
    payload: SaleCreateRequest,
    x_tenant_id: Optional[str] = Header(default=None, alias="X-Tenant-ID"),
) -> dict:
    total_amount = payload.quantity * payload.unit_price_ugx

    sale_record = {
        "sale_id": str(uuid4()),
        "tenant_id": payload.tenant_id,
        "item_sku": payload.item_sku.strip(),
        "quantity": payload.quantity,
        "unit_price_ugx": payload.unit_price_ugx,
        "total_amount_ugx": total_amount,
        "currency": "UGX",
        "recorded_at": datetime.now(timezone.utc).isoformat(),
    }

    SALES_STORE.append(sale_record)
    return {"status": "success", "data": sale_record}
