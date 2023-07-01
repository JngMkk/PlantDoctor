from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from core.db import get_async_session

SESSION: AsyncSession = Depends(get_async_session)
