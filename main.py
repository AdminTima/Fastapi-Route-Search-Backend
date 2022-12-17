from fastapi import FastAPI
from app.cities.router import cities_router

app = FastAPI()

app.include_router(cities_router, prefix="/cities")

@app.get("/")
def index():
    return {"msg": "success"}
