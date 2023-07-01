from fastapi import FastAPI

from apps.users.routes import USERS_ROUTER
from common.schemas.exceptions import InternalServerValidationExceptionResp
from core.handlers import EXCEPTION_HANDLER


def init_fastapi_app() -> FastAPI:
    app = FastAPI(
        debug=True,
        title="PlantDoctor v2",
        description="PlantDoctor v2 APIs",
        version="v2",
        docs_url="/swagger",
        terms_of_service="https://www.google.com/policies/terms/",
        exception_handlers=EXCEPTION_HANDLER,
        responses={422: {"model": InternalServerValidationExceptionResp}},
    )

    app.include_router(USERS_ROUTER)
    return app
