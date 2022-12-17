from fastapi import FastAPI
from app.cities.router import cities_router
from app.trains.router import trains_router
from app.middleware.exceptions_middleware import handle_exceptions_middleware

app = FastAPI()
app.middleware("http")(handle_exceptions_middleware)

app.include_router(cities_router, prefix="/cities")
app.include_router(trains_router, prefix="/trains")


@app.get("/")
def index():
    return {"msg": "success"}
