from ..base.base_repository import BaseRepository
from .models import Trains
from .repository import TrainsRepository
from .schemas import TrainSchema
from ..base.base_api_exception import BaseApiException


@TrainsRepository.get_repo
def create_train(repo: TrainsRepository, train_data: TrainSchema):
    train_in_db = repo.find_trains_by_cities(
        train_data.from_city_id,
        train_data.to_city_id
    )
    if len(train_in_db):
        for train in train_in_db:
            print(train.__dict__)
            if train.travel_time == train_data.travel_time:
                raise BaseApiException.bad_request("Such entry already exists")
    return repo.create(Trains, train_data.dict())


@BaseRepository.get_repo
def remove_train(repo: BaseRepository, train_id):
    train_in_db = repo.get_by_id(Trains, train_id)
    if not train_in_db:
        raise BaseApiException.not_found()
    return repo.remove_by_id(Trains, train_id)


@BaseRepository.get_repo
def update_train(repo: BaseRepository, train_id, updated_data):
    train_in_db = repo.get_by_id(Trains, train_id)
    if not train_in_db:
        raise BaseApiException.not_found()
    return repo.update_by_id(Trains, train_id, updated_data)


@BaseRepository.get_repo
def get_all_trains(repo: BaseRepository):
    return repo.get_all(Trains)


