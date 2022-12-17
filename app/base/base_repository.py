from ..db_config import Session
from sqlalchemy import select


class BaseRepository:

    def __init__(self):
        self.session = Session()

    def create(self, new_obj):
        self.session.add(new_obj)
        self.session.commit()
        self.session.refresh(new_obj)
        return new_obj

    def remove(self, obj_for_delete):
        self.session.delete(obj_for_delete)
        self.session.commit()

    def get_by_id(self, table, obj_id):
        query = select(table).filter_by(id=obj_id)
        result = self.session.execute(query).scalar()
        return result

    def get_all(self, table):
        query = select(table)
        return self.session.execute(query).scalars().all()

    def execute_query(self, query, commit=False):
        result = self.session.execute(query)
        if commit:
            self.session.commit()
        return result

    @classmethod
    def get_repo(cls, func):
        def wrapper(*args, **kwargs):
            db = cls()
            try:
                result = func(db, *args, **kwargs)
            finally:
                db.session.close()
            return result
        return wrapper
