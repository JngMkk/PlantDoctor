from typing import Any

__all__ = ["PlantDoctorException", "NotAuthenticated", "Forbidden", "InternalServerValidationException"]


class PlantDoctorException(Exception):
    status_code: int
    error_code: int
    error_msg: str
    error_data: Any | None = None

    def __init__(self, error_data: Any | None = None) -> None:
        self.error_data = error_data


class NotAuthenticated(PlantDoctorException):
    status_code = 401
    error_code = 1000
    error_msg = "인증된 요청이 아닙니다."


class Forbidden(PlantDoctorException):
    status_code = 403
    error_code = 1001
    error_msg = "접근할 수 없습니다."


class InternalServerValidationException(PlantDoctorException):
    status_code = 422
    error_code = 1003
    error_msg = "UNPROCESSABLE_ENTITY"
