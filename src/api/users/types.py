import datetime

import strawberry
from pydantic import typing

from db import models
from api.student_data.types import StudentData
from api.student_data.query import StudentDataQuery
from db.resolvers import get_absents


@strawberry.type
class User:
    id: int
    surname: str
    name: str
    middle_name: typing.Optional[str]
    snils: typing.Optional[str]
    inn: typing.Optional[str]
    email: typing.Optional[str]
    phone: typing.Optional[str]
    study_year: int

    @strawberry.field
    async def student_data(self) -> "StudentData":
        return await StudentDataQuery().student_data(user_id=self.id)

    @strawberry.field
    async def absents(self) -> typing.List["Absents"]:
        absents = await get_absents(self.id)
        return [Absents.marshal(absent) for absent in absents]

    @classmethod
    def marshal(cls, model: models.User) -> "User":
        return cls(
            id=model.id,
            surname=model.surname,
            name=model.name,
            middle_name=model.middle_name,
            snils=model.snils,
            inn=model.inn,
            email=model.email,
            phone=model.phone,
            study_year=model.study_year
        )


@strawberry.type
class Absents:
    id: int
    # user_id = Column(ForeignKey("users.id"))
    date: datetime.date
    class_number: int

    @classmethod
    def marshal(cls, model: models.Absenteeism) -> "Absents":
        return cls(
            id=model.id,
            date=model.date,
            class_number=model.class_number
        )


# @strawberry.input
# class UserInput:
#     surname: str
#     name: str
#     middle_name: typing.Optional[str]
#     snils: typing.Optional[str]
#     inn: typing.Optional[str]
#     email: typing.Optional[str]
#     phone: typing.Optional[str]
#     study_year: int

