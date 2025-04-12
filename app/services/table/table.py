from typing import Sequence

from app.models import Table

from app.schemas.table import TableCreate

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

async def get_all_tables(
    session: AsyncSession,
) -> Sequence[Table]:
    stmt = select(Table).order_by(Table.id)
    result = await session.scalars(stmt)
    return result.all()


async def create_table(
    session: AsyncSession,
    table_create: TableCreate,
) -> Table:
    table = Table(**table_create.model_dump())
    session.add(table)
    await session.commit()
    return table


async def delete_table(
    session: AsyncSession,
    table_id: int,
) -> Table:
    table = await session.execute(select(Table).where(Table.id == table_id))
    table = table.scalar_one()
    await session.delete(table)
    await session.commit()
    return table