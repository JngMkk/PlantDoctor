import re
from typing import Any

from pydantic import BaseModel, EmailStr, Field, root_validator

from core.config import settings

PW_REGEX = settings.PW_CONFIG["PW_REGEX"]


class TokenResponse(BaseModel):
    accessToken: str

    class Config:
        schema_extra = {"access_token": "ACCESS TOKEN"}


class ReadUser(BaseModel):
    id: int
    email: str


class SignUpBody(BaseModel):
    email: EmailStr
    pw: str = Field(max_length=20, regex=PW_REGEX)
    pw2: str = Field(max_length=20, regex=PW_REGEX)

    @root_validator()
    def validate_pw(cls, values: dict[str, Any]) -> dict[str, Any]:
        pw = values["pw"]
        if re.fullmatch(PW_REGEX, pw) is None:
            raise ValueError("비밀번호 형식이 올바르지 않습니다.")
        if pw != values["pw2"]:
            raise ValueError("입력한 두 비밀번호가 같지 않습니다.")

        return values


class LoginBody(BaseModel):
    email: EmailStr
    pw: str = Field(max_length=20)
