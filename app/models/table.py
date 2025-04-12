from .base import Base
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import CheckConstraint

class Table(Base):
    
    name: Mapped[str] = mapped_column(nullable=False)
    seats: Mapped[int] = mapped_column(nullable=False)
    location: Mapped[str] = mapped_column(nullable=False)

    reservation: Mapped[list["Reservation"]] = relationship(
        back_populates="table",
    )

    __table_args__ = (
        CheckConstraint("seats > 0", name="check_seats_positive"),
    )