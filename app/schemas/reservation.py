from .base import Base
from datetime import datetime

class ReservationBase(Base):
    customer_name: str
    table_id: int
    reservation_time: datetime
    duration_minutes: int

class ReservationRead(ReservationBase):
    id: int

class ReservationCreate(ReservationBase):
    pass

class ReservationDelete(ReservationBase):
    id: int
