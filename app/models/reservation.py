from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.types import TIMESTAMP
from .table import Table
from datetime import datetime

class Reservation(Base):
    
    customer_name: Mapped[str] = mapped_column(nullable=False)
    table_id: Mapped[int] = mapped_column(ForeignKey(f"{Table.__tablename__}.id"), nullable=False)
    reservation_time: Mapped[datetime] = mapped_column(type_=TIMESTAMP(timezone=True), nullable=False)
    duration_minutes: Mapped[int] = mapped_column(nullable=False)

    table: Mapped["Table"] = relationship(
        back_populates="reservation"
    )

    __table_args__ = (
        CheckConstraint("duration_minutes > 0", name="check_duration_positive"),
    )
