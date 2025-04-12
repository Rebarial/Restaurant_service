from fastapi import APIRouter, Depends, HTTPException
from services.reservation import reservation
from app.schemas.reservation import ReservationCreate
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.database import db_helper

router = APIRouter(
    tags=["Reservation"]
)

@router.get("/")
async def get_tables(
    session: AsyncSession = Depends(db_helper.session_getter)
    ):
    result = await reservation.get_all_reservations(session=session)

    return result

@router.post("/")
async def create_table(
    reservation_create: ReservationCreate,
    session: AsyncSession = Depends(db_helper.session_getter),
    ):
    result = await reservation.create_reservation(session=session, reservation_create=reservation_create)

    if isinstance(result, dict) and "error" in result:
        if result["error"]["error_type"] == "ValidationError":
            raise HTTPException(
                status_code=400,
                detail=result["error"]["error_message"]
            )

    return result

@router.delete("/")
async def delete_table(
    reservation_id: int,
    session: AsyncSession = Depends(db_helper.session_getter),
    ):
    result = await reservation.delete_reservation(session=session, reservation_id=reservation_id)

    return result
