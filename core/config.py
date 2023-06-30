import json
import os
from functools import lru_cache
from typing import Any, Final

from pydantic import AnyUrl, BaseSettings
from sqlmodel.ext.asyncio.session import AsyncSession


def get_config() -> dict[str, Any]:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(base_dir, "config.json")

    try:
        file = open(config_file, "r")
        data = file.read()
        config = json.loads(data)
        file.close()
    except FileNotFoundError:
        raise FileNotFoundError("There is no config file.")

    return config


def get_db_uri() -> Any:
    scheme = "mysql+aiomysql"
    user = os.getenv("PLANTDOCTOR_DB_USER", "root")
    pw = os.getenv("PLANTDOCTOR_DB_PW")  # type:ignore
    host = "localhost"
    port = os.getenv("PLANTDOCTOR_DB_PORT", "3306")
    path = os.getenv("PLANTDOCTOR_DB")  # type:ignore
    query = "charset=utf8mb4"

    if not all((user, pw, path)):
        raise ValueError("Database user, password, path are required.")

    port += "/"
    return AnyUrl.build(scheme=scheme, user=user, password=pw, host=host, port=port, path=path, query=query)


# ===========================================================================================================
CONFIG: Final[dict[str, Any]] = get_config()


class Settings(BaseSettings):
    DB_URI: str = get_db_uri()
    ENGINE_CONFIG: dict[str, Any] = {
        "future": True,
        "pool_pre_ping": True,
        "pool_size": 5,
        "max_overflow": 64,
    }
    SESSION_CONFIG: dict[str, Any] = {
        "class_": AsyncSession,
        "autoflush": False,
        "autocommit": False,
        "expire_on_commit": False,
    }

    SIGNIN_API_URI: str = "/users/signin"
    JWT_CONFIG: dict[str, Any] = CONFIG["JWT"]
    USER_ID_FIELD: str = "id"
    USER_EMAIL_FIELD: str = "email"
    PW_CONFIG: dict[str, Any] = CONFIG["PW"]


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
