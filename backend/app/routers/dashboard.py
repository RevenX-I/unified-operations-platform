from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import func, select
from ..database import get_db
from ..models import Booking, Contact, InventoryItem

router = APIRouter(
    prefix="/dashboard",
    tags=["dashboard"],
)

@router.get("/stats")
async def get_dashboard_stats(db: AsyncSession = Depends(get_db)):
    # Mock data or real queries
    # For now return placeholder
    return {
        "today_bookings": 0,
        "upcoming_bookings": 0,
        "new_inquiries": 0,
        "pending_forms": 0,
        "low_stock_items": 0,
        "alerts": []
    }
