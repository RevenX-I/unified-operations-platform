from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..database import get_db
from ..models import Workspace, User
from ..schemas import user as user_schema # Need workspace schema
# from ..utils import get_current_user

router = APIRouter(
    prefix="/workspaces",
    tags=["workspaces"],
)

@router.post("/", response_model=dict)
async def create_workspace(name: str, db: AsyncSession = Depends(get_db)):
    # simplified
    new_ws = Workspace(name=name)
    db.add(new_ws)
    await db.commit()
    await db.refresh(new_ws)
    return {"id": new_ws.id, "name": new_ws.name}

@router.get("/my", response_model=dict)
async def get_my_workspace(db: AsyncSession = Depends(get_db)):
    # Mocked user context
    return {"message": "Not implemented yet"}
