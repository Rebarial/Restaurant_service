from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import timedelta
from app.models import Reservation
from app.schemas.reservation import ReservationCreate
from sqlalchemy import or_, and_, not_
from sqlalchemy.sql import func
import asyncio
from sqlalchemy.sql import func

async def is_table_taken(
        reservation_create: ReservationCreate,
        session: AsyncSession
        ) -> bool:
    end_time = reservation_create.reservation_time + timedelta(minutes=reservation_create.duration_minutes)
    
    query = (
        select(Reservation).where(
            and_(
                Reservation.table_id == reservation_create.table_id,

                not_(
                    or_(
                    Reservation.reservation_time + (Reservation.duration_minutes * func.make_interval(0, 0, 0, 0, 0, 1, 0)) < reservation_create.reservation_time,
                    Reservation.reservation_time > end_time
                    )
                )
            )
        )
    )

    result = await session.scalars(query)

    result = len(result.all())

    if result > 0:
        return True

    return False
    