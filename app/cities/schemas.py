from pydantic import BaseModel


class CitySchema(BaseModel):
    name: str

    class Config:
        orm_mode = True


class CityOutSchema(CitySchema):
    id: int


