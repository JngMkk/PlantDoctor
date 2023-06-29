from typing import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from .config import settings

db_engine = create_async_engine(settings.DB_URI, **settings.ENGINE_CONFIG)
db_session = sessionmaker(bind=db_engine, **settings.SESSION_CONFIG)


async def get_async_session() -> AsyncIterator[AsyncSession]:
    async with db_session() as db:
        yield db
