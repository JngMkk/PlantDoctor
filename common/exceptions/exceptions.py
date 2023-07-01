from typing import Any

__all__ = [
    "PlantDoctorException",
    "NotAuthenticated",
    "Forbidden",
    "InternalServerValidationException",
    "NotFound",
    "ResourceAlreadyExists",
]


class PlantDoctorException(Exception):
    status_code: int
    error_code: str
    error_msg: str | None
    error_data: Any | None = None

    def __init__(self, error_msg: str | None = None, error_data: Any | None = None) -> None:
        self.error_msg = error_msg or self.error_msg
        self.error_data = error_data


class NotFound(PlantDoctorException):
    status_code = 400
    error_code = "NOT_FOUND"
    error_msg = "자원을 찾을 수 없습니다."


class NotAuthenticated(PlantDoctorException):
    status_code = 401
    error_code = "NOT_AUTHENTICATED"
    error_msg = "인증된 요청이 아닙니다."


class Forbidden(PlantDoctorException):
    status_code = 403
    error_code = "FORBIDDEN"
    error_msg = "접근할 수 없습니다."


class ResourceAlreadyExists(PlantDoctorException):
    status_code = 409
    error_code = "RESOURCE_ALREADY_EXISTS"
    error_msg = "이미 존재하는 값입니다."


class InternalServerValidationException(PlantDoctorException):
    status_code = 422
    error_code = "VALIDATION_ERROR"
    error_msg = "서버 내 데이터 검증 오류가 발생했습니다."
