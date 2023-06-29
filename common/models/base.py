from datetime import datetime

from sqlmodel import Field, SQLModel

from common.utils.timezone import kst_now


class BaseModel(SQLModel):
    createdAt: datetime | None = Field(default_factory=kst_now)
    updatedAt: datetime | None = Field(default_factory=kst_now, sa_column_kwargs={"onupdate": kst_now})
