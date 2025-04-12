from .base import Base

class TableBase(Base):
    name: str
    seats: int
    location: str

class TableRead(TableBase):
    id: int

class TableCreate(TableBase):
    pass

class TableDelete(TableBase):
    id: int
