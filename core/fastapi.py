from fastapi import FastAPI


def init_fastapi_app() -> FastAPI:
    app = FastAPI(
        debug=True,
        title="PlantDoctor v2",
        description="PlantDoctor v2 APIs",
        version="v2",
        docs_url="/swagger",
        terms_of_service="https://www.google.com/policies/terms/",
    )
    return app
