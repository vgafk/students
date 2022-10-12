import strawberry
from typing import List, Optional

from db import models
from api.student_data.types import StudentData
from api.student_data.query import StudentDataQuery
from api.absents.types import Absents
from api.absents.query import AbsentQuery


@strawberry.type
class User:
    id: int
    surname: str
    name: str
    middle_name: Optional[str]
    snils: Optional[str]
    inn: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    study_year: int

    @strawberry.field
    async def student_data(self) -> "StudentData":
        return await StudentDataQuery().student_data(user_id=self.id)

    @strawberry.field
    async def absents(self) -> List["Absents"]:
        return AbsentQuery().absent(user_id=self.id)

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

