from ..base.base_api_exception import BaseApiException
from fastapi.responses import JSONResponse


async def handle_exceptions_middleware(request, call_next):
    try:
        print("middle try")
        result = await call_next(request)
    except BaseApiException as err:
        print("middle base exc")
        return JSONResponse({"msg": err.message}, err.status)
    except Exception as err:
        print("mid exc")
        print(err)
        return JSONResponse({"msg": "Internal server error"}, 500)
    return result

