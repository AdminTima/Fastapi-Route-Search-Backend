from pydantic import BaseModel


class TrainSchema(BaseModel):
    name: str
    from_city_id: int
    to_city_id: int
    travel_time: int

    class Config:
        orm_mode = True


class TrainOutSchema(TrainSchema):
    id: int

