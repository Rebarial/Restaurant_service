from pydantic import BaseModel

class Base(BaseModel):

    def __repr__(self):
        result = f"{self.__class__.__name__}: "
        for key in self.__table__.columns.keys():
            result += f" {key}:{getattr(self, key)}"
        return result