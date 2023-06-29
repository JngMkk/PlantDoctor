from sqlalchemy import Column
from sqlalchemy.dialects.mysql import SMALLINT, TEXT, TINYINT
from sqlmodel import Field, SQLModel


class WaterCycle(SQLModel):
    __tablename__ = "waterCycle"

    id: int | None = Field(
        default=None, sa_column=Column(TINYINT), primary_key=True, description="water cycle ID"
    )
    description: str = Field(max_length=8, description="cycle info")


class WaterMethod(SQLModel):
    __tablename__ = "waterMethod"

    id: int | None = Field(
        default=None, sa_column=Column(TINYINT), primary_key=True, description="how to water ID"
    )
    description: str = Field(max_length=40, description="how to water info")


class WaterMethodDetail(SQLModel):
    __tablename__ = "waterMethodDetail"

    id: int | None = Field(
        default=None, sa_column=Column(TINYINT), primary_key=True, description="how to water detail ID"
    )
    description: str = Field(max_length=20, description="how to water detail info")


class LightLocation(SQLModel):
    __tablename__ = "lightLocation"

    id: int | None = Field(
        default=None, sa_column=Column(TINYINT), primary_key=True, description="light location ID"
    )
    description: str = Field(max_length=10, description="light location info")


class LightSumm(SQLModel):
    __tablename__ = "lightSumm"

    id: int | None = Field(
        default=None, sa_column=Column(TINYINT), primary_key=True, description="light summ ID"
    )
    description: str = Field(max_length=30, description="light summ info")


class HumidEnv(SQLModel):
    __tablename__ = "humidEnv"

    id: int | None = Field(
        default=None, sa_column=Column(TINYINT), primary_key=True, description="humid env ID"
    )
    description: str = Field(max_length=20, description="humid env info")


class HumidSumm(SQLModel):
    __tablename__ = "humidSumm"

    id: int | None = Field(
        default=None, sa_column=Column(TINYINT), primary_key=True, description="humid summ ID"
    )
    description: str = Field(max_length=30, description="humid summ info")


class tempEnv(SQLModel):
    __tablename__ = "tempEnv"

    id: int | None = Field(
        default=None, sa_column=Column(TINYINT), primary_key=True, description="temp env ID"
    )
    description: str = Field(max_length=20, description="temp env info")


class Plant(SQLModel):
    __tablename__ = "plants"

    id: int | None = Field(default=None, sa_column=Column(SMALLINT), primary_key=True, description="식물 ID")
    image: str = Field(max_length=255, description="식물 이미지 URL")
    koNm: str = Field(max_length=16, description="식물 이름(한국어)")
    enNm: str = Field(max_length=64, description="식물 이름(영어)")
    summ: str = Field(max_length=128, description="간단한 정보(요약)")
    waterCycleId: int = Field(description="water cycle ID")
    waterMethodId: int = Field(description="how to water ID")
    waterMethodDetailId: int = Field(description="how to water detail ID")
    lightLocationId: int = Field(description="light location ID")
    lightSummId: int = Field(description="light summ ID")
    humidEnvId: int = Field(description="humid env ID")
    humidSummId: int = Field(description="humid summ ID")
    tempEnvId: int = Field(description="temp env ID")
    waterDetail: str = Field(sa_column=Column(TEXT), description="물주기 상세 정보")
    lightDetail: str = Field(sa_column=Column(TEXT), description="빛 상세 정보")
    humidDetail: str = Field(sa_column=Column(TEXT), description="습도 상세 정보")
    tempDetail: str = Field(sa_column=Column(TEXT), description="온도 상세 정보")


class PlantDisease(SQLModel):
    __tablename__ = "plantDiseases"

    id: int | None = Field(default=None, sa_column=Column(TINYINT), primary_key=True, description="식물 질병 ID")
    koNm: str = Field(max_length=10, description="질병명(한국어)")
    enNm: str = Field(max_length=20, description="질병명(영어)")
    symptom: str = Field(sa_column=Column(TEXT), description="증상")
    env: str = Field(sa_column=Column(TEXT), description="환경")
    precaution: str = Field(sa_column=Column(TEXT), description="예방법")
