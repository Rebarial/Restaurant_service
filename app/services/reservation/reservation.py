from typing import Sequence

from app.models import Reservation

from app.schemas.reservation import ReservationCreate

from . import validation

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

def dateadd(date_field, interval):
    return date_field + interval

async def get_all_reservations(
    session: AsyncSession,
) -> Sequence[Reservation]:
    stmt = select(Reservation).order_by(Reservation.id)
    result = await session.scalars(stmt)
    return result.all()

async def create_reservation(
    session: AsyncSession,
    reservation_create: ReservationCreate,
) -> Reservation:
    reservation = Reservation(**reservation_create.model_dump())

    if await validation.is_table_taken(reservation_create=reservation_create, session=session):
        return {"error": 
                    {
                        "error_type": "ValidationError",
                        "error_message": "The table had already been reserved."
                    }
                }

    session.add(reservation)
    await session.commit()
    return reservation



async def delete_reservation(
    session: AsyncSession,
    reservation_id: int,
) -> Reservation:
    reservation = await session.execute(select(Reservation).where(Reservation.id == reservation_id))
    reservation = reservation.scalar_one()
    await session.delete(reservation)
    await session.commit()
    return reservation