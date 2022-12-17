from ..base.base_repository import BaseRepository
from .repository import CitiesRepository
from .models import Cities
from ..base.base_api_exception import BaseApiException


@CitiesRepository.get_repo
def create_city(repo: CitiesRepository, city_data):
    city_in_db = repo.get_city_by_name(city_data["name"])
    if city_in_db:
        raise BaseApiException.bad_request("Such entry already exists")
    return repo.create(Cities, city_data)


@BaseRepository.get_repo
def update_city(repo: BaseRepository, city_id, new_data):
    return repo.update_by_id(Cities, city_id, new_data)


@BaseRepository.get_repo
def remove_city(repo: BaseRepository, city_id):
    city_in_db = repo.get_by_id(Cities, city_id)
    if not city_in_db:
        raise BaseApiException.not_found("Not found such city")
    return repo.remove_by_id(Cities, city_id)


@BaseRepository.get_repo
def get_all_cities(repo: BaseRepository):
    return repo.get_all(Cities)


@BaseRepository.get_repo
def get_city(repo: BaseRepository, city_id):
    city = repo.get_by_id(Cities, city_id)
    if not city:
        raise BaseApiException.bad_request("No city with provided id")
    return city


