from datetime import timedelta
from typing import Any

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from common.exceptions import Forbidden, NotAuthenticated
from common.models.users import User
from common.utils.timezone import kst_now

from .config import settings
from .db import get_async_session

# * schemes: 해시 알고리즘 list
# * deprecated="auto": 지정 해시 알고리즘을 제외하고 지원되는 모든 알고리즘을 사용하지 않음.
pw_context = CryptContext(schemes=[settings.PW_CONFIG["PW_HASH_ALGORITHM"]], deprecated="auto")

# * OAuth2PasswordBearer: FastAPI에서 제공하는 보안 로직
# * Application에 보안 로직이 존재함을 알림
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=settings.SIGNIN_API_URI, auto_error=False)


class HashPW:
    @staticmethod
    def create_hash(password: str) -> str:
        """문자열 해싱한 값 반환"""
        return pw_context.hash(password)

    @staticmethod
    def check_password(plain_password: str, hashed_password: str) -> bool:
        """일반 패스워드와 해싱한 패스워드가 일치하는지 비교한 후 True/False 반환"""
        return pw_context.verify(plain_password, hashed_password)


def create_access_token(data: dict[str, Any]) -> str:
    jwt_config = settings.JWT_CONFIG

    to_encode = data.copy()
    expire = kst_now() + timedelta(seconds=jwt_config["TOKEN_EXPIRE_SECONDS"])
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, jwt_config["JWT_SECRET_KEY"], jwt_config["JWT_ALGORITHM"])
    return token


# * token에 oauth2_scheme 의존성 주입
async def authenticate(
    token: str = Depends(oauth2_scheme), session: AsyncSession = Depends(get_async_session)
) -> User:
    jwt_config = settings.JWT_CONFIG

    try:
        payload = jwt.decode(token, jwt_config["JWT_SECRET_KEY"], jwt_config["JWT_ALGORITHM"])
        user_id = payload.get(settings.USER_ID_FIELD)
        if user_id is None:
            raise NotAuthenticated
    except JWTError:
        raise NotAuthenticated

    q = select(User).where(User.id == user_id)
    resp = await session.execute(q)
    user: User | None = resp.scalar_one_or_none()
    if user is None:
        raise NotAuthenticated
    if user is not None:
        if not user.isActive:
            raise Forbidden
    return user
