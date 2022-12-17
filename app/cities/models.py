from ..db_config import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String


class Cities(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)



