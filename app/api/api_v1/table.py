from fastapi import APIRouter, Depends
from services.table import table
from app.schemas.table import TableCreate
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.database import db_helper

router = APIRouter(
    tags=["Tables"]
)

@router.get("/")
async def get_tables(
    session: AsyncSession = Depends(db_helper.session_getter)
    ):
    result = await table.get_all_tables(session=session)
    return result

@router.post("/")
async def create_table(
    table_create: TableCreate,
    session: AsyncSession = Depends(db_helper.session_getter),
    ):
    result = await table.create_table(session=session, table_create=table_create)
    return result

@router.delete("/")
async def delete_table(
    table_id: int,
    session: AsyncSession = Depends(db_helper.session_getter),
    ):
    result = await table.delete_table(session=session, table_id=table_id)
    return result
