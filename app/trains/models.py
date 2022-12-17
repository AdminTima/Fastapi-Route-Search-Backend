from ..db_config import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Trains(Base):
    __tablename__ = "trains"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    from_city_id = Column(Integer, ForeignKey("cities.id"), nullable=False)
    to_city_id = Column(Integer, ForeignKey("cities.id"), nullable=False)
    travel_time = Column(Integer, nullable=False)

    in_city = relationship("Cities", foreign_keys=[to_city_id])
    out_city = relationship("Cities", foreign_keys=[from_city_id])




