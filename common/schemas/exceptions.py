from typing import Any

from pydantic import BaseModel

from common.exceptions import *  # type: ignore


def init_schema_extra(cls: type[PlantDoctorException]) -> dict[str, dict[str, Any]]:
    _vars = {"status_code", "error_code", "error_msg", "error_data"}

    return {"example": {k: v for k, v in vars(cls).items() if k in _vars}}


class ExceptionRespBase(BaseModel):
    status_code: int
    error_code: int
    error_msg: str
    error_data: Any | None


class NotAuthenticatedRespSchema(ExceptionRespBase):
    class Config:
        schema_extra = init_schema_extra(NotAuthenticated)


class ForbiddenRespSchema(ExceptionRespBase):
    class Config:
        schema_extra = init_schema_extra(Forbidden)


class InternalServerValidationExceptionRespSchema(ExceptionRespBase):
    class Config:
        schema_extra = init_schema_extra(InternalServerValidationException)
