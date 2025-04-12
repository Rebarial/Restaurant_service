from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import declared_attr
from sqlalchemy import MetaData
from app.config import settings

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    __abstract__ = True

    metadata = MetaData(
        naming_convention=settings.naming_conventions
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
    

    def __repr__(self):
        result = f"{self.__class__.__name__}: "
        for key in self.__table__.columns.keys():
            result += f" {key}:{getattr(self, key)}"
        return result
        