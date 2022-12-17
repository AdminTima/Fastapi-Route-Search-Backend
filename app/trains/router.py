from fastapi import APIRouter
from .schemas import TrainSchema, TrainOutSchema
from . import service


trains_router = APIRouter()


@trains_router.get("/", response_model=list[TrainOutSchema])
def get_all():
    return service.get_all_trains()


@trains_router.post("/", response_model=TrainOutSchema)
def create_train(train_data: TrainSchema):
    return service.create_train(train_data)


@trains_router.put("/{train_id}", response_model=TrainOutSchema)
def update_train(train_id: int, updated_data: TrainSchema):
    return service.update_train(train_id, updated_data.dict())


@trains_router.delete("/{train_id}", response_model=TrainOutSchema)
def remove_train(train_id: int):
    return service.remove_train(train_id)





