from fastapi.exceptions import HTTPException


class BaseApiException(Exception):

    def __init__(self, message, status):
        self.message = message
        self.status = status

    @staticmethod
    def bad_request(msg="Bad request"):
        return BaseApiException(msg, 400)

    @staticmethod
    def forbidden(msg="Forbidden"):
        return BaseApiException(msg, 403)

    @staticmethod
    def not_found(msg="Not found"):
        return BaseApiException(msg, 404)

    @staticmethod
    def unauthorized(msg="Unauthorized"):
        return BaseApiException(msg, 401)
