from ..db_config import Session
from sqlalchemy import select, update, delete, literal_column


class BaseRepository:

    def __init__(self):
        self.session = Session()

    def create(self, table,  new_obj_data):
        new_obj = table(**new_obj_data)
        self.session.add(new_obj)
        self.session.commit()
        self.session.refresh(new_obj)
        return new_obj

    def remove_by_id(self, table, obj_id):
        query = (delete(table)
                 .where(table.id == obj_id)
                 .returning(table)
                )
        return self.execute_query(query, commit=True).one()

    def get_by_id(self, table, obj_id):
        query = select(table).filter_by(id=obj_id)
        result = self.session.execute(query).scalar()
        return result

    def update_by_id(self, table, obj_id, updated_data):
        query = (
            update(table)
            .where(table.id == obj_id)
            .values(**updated_data)
            .returning(table)
        )
        return self.execute_query(query, commit=True).one()

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
            repo = cls()
            try:
                result = func(repo, *args, **kwargs)
            finally:
                repo.session.close()
            return result
        return wrapper
