from ..base.base_repository import BaseRepository
from .models import Cities
from sqlalchemy import select
from sqlalchemy import update


class CitiesRepository(BaseRepository):

    def get_all_cities(self):
        return self.get_all(Cities)

    def create_city(self, name):
        new_city = Cities(name=name)
        return self.create(new_city)

    def get_city_by_name(self, name):
        query = select(Cities).filter_by(name=name)
        return self.execute_query(query)

    def get_city_by_id(self, obj_id):
        return self.get_by_id(Cities, obj_id)

    def remove_city(self, obj_for_remove):
        return self.remove(obj_for_remove)

    def update_city(self, obj_id, kwargs):
        query = (update(Cities)
                 .where(Cities.id == obj_id)
                 .values(**kwargs)
                 .returning(Cities.name))
        return self.execute_query(query, commit=True).scalar()



