from datetime import datetime

from pydantic import EmailStr
from sqlmodel import Field

from .base import BaseModel


class User(BaseModel, table=True):
    __tablename__ = "users"

    id: int | None = Field(default=None, primary_key=True, description="회원 ID")
    userName: str = Field(max_length=20, description="유저 이름")
    email: EmailStr = Field(max_length=100, description="이메일")
    password: str = Field(max_length=64, description="비밀번호")
    isAdmin: bool | None = Field(default=False, description="관리자 여부")
    isActive: bool | None = Field(default=True, description="비활성 여부")
    lastLogin: datetime | None = Field(default=None, description="마지막 로그인")
