from .repository import CitiesRepository


@CitiesRepository.get_repo
def create_city(repo, name):
    city_in_db = repo.get_city_by_name(name).scalar()
    if city_in_db:
        raise Exception("Already exists")
    return repo.create_city(name)


@CitiesRepository.get_repo
def update_city(repo, city_id, new_data):
    return repo.update_city(city_id, new_data)


@CitiesRepository.get_repo
def remove_city(repo, city_id):
    city_in_db = repo.get_city_by_id(city_id)
    if not city_in_db:
        raise Exception("Not found")
    repo.remove_city(city_in_db)
    return city_in_db


@CitiesRepository.get_repo
def get_all_cities(repo):
    return repo.get_all_cities()



