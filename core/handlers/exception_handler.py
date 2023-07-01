import logging
from typing import Any, Callable, Final

from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from fastapi.exceptions import RequestValidationError as _RequestValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse

from common.exceptions import InternalServerValidationException, PlantDoctorException


def init_error(exc: PlantDoctorException | HTTPException) -> dict[str, Any]:
    error_resp = {
        "error": {
            "status_code": getattr(exc, "status_code"),
            "error_code": getattr(exc, "error_code"),
            "error_msg": getattr(exc, "error_msg", "알 수 없는 오류가 발생했습니다."),
            "error_data": getattr(exc, "error_data", None),
        },
    }
    logging.error(error_resp["error"])
    return error_resp


async def http_exception_handler(request: Request, exc: PlantDoctorException | HTTPException) -> JSONResponse:
    return JSONResponse(content=init_error(exc), status_code=exc.status_code)


async def request_validation_exception_handler(
    request: Request, exc: _RequestValidationError
) -> JSONResponse:
    error_body = jsonable_encoder(exc.errors())
    exception = InternalServerValidationException(error_data=error_body)
    return JSONResponse(content=init_error(exception), status_code=exception.status_code)


EXCEPTION_HANDLER: Final[dict[Any, Callable]] = {
    HTTPException: http_exception_handler,
    PlantDoctorException: http_exception_handler,
    _RequestValidationError: request_validation_exception_handler,
}
