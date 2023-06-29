import os
from functools import lru_cache
from typing import Any

from pydantic import AnyUrl, BaseSettings
from sqlmodel.ext.asyncio.session import AsyncSession


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


class Settings(BaseSettings):
    # * DB Connection
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


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
