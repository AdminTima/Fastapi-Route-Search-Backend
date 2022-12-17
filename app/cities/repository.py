from ..base.base_repository import BaseRepository
from .models import Cities
from sqlalchemy import select


class CitiesRepository(BaseRepository):
    def get_city_by_name(self, city_name):
        query = select(Cities).filter_by(name=city_name)
        return self.execute_query(query).scalar()


