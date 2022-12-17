from fastapi import APIRouter
from . import service
from .schemas import CityOutSchema, CitySchema
from typing import List


cities_router = APIRouter()


@cities_router.get("/", response_model=List[CityOutSchema])
def get_all():
    return service.get_all_cities()


@cities_router.post("/", response_model=CityOutSchema)
def create_city(city: CitySchema):
    return service.create_city(city.name)


@cities_router.delete("/{city_id}", response_model=CityOutSchema)
def remove_city(city_id: int):
    return service.remove_city(city_id)


@cities_router.put("/{city_id}")
def update_city(city_id: int, new_city_data: CitySchema):
    return service.update_city(city_id, new_city_data.dict())


