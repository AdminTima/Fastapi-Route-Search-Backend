from ..base.base_repository import BaseRepository
from sqlalchemy import select
from .models import Trains


class TrainsRepository(BaseRepository):

    def find_trains_by_cities(self, from_city_id, to_city_id):
        query = (select(Trains)
                 .where(Trains.from_city_id == from_city_id,
                        Trains.to_city_id == to_city_id
                        )
                 )
        return self.execute_query(query).scalars().all()


