from datetime import timedelta

from fastapi import APIRouter, Body
from sqlalchemy.exc import NoResultFound
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from common.constant.depends import SESSION
from common.exceptions import Forbidden, NotFound, ResourceAlreadyExists
from common.models.users import User
from common.utils.timezone import kst_now
from core.auth import Auth
from core.config import settings

from .schemas import LoginBody, ReadUser, SignUpBody, TokenResponse

USERS_ROUTER = APIRouter(prefix="/users", tags=["Users"])


@USERS_ROUTER.post("/signup", status_code=201, response_model=ReadUser)
async def user_signup(signup_body: SignUpBody = Body(), session: AsyncSession = SESSION) -> User:
    q = select(User).where(User.email == signup_body.email)
    resp = await session.execute(q)
    try:
        resp.scalar_one()
        raise ResourceAlreadyExists
    except NoResultFound:
        pass

    hashed_pw = Auth.create_hash_pw(signup_body.pw)
    signup_body.pw = hashed_pw

    user = User.from_orm(signup_body)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


@USERS_ROUTER.post("/signin", status_code=200, response_model=TokenResponse)
async def user_login(login_body: LoginBody = Body(), session: AsyncSession = SESSION) -> dict[str, str]:
    q = select(User).where(User.email == login_body.email)
    resp = await session.execute(q)
    try:
        user: User = resp.scalar_one()
    except NoResultFound:
        raise NotFound

    if not Auth.check_pw(login_body.pw, user.pw):
        raise Forbidden

    expire = kst_now() + timedelta(seconds=settings.JWT_CONFIG["TOKEN_EXPIRE_SECONDS"])
    jwt_payload = {"exp": expire, "aud": user.id, "is_admin": user.isAdmin}
    access_token = Auth.create_access_token(jwt_payload)
    return {"accessToken": access_token}
