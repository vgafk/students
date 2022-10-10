from datetime import date

import strawberry
from pydantic import typing
from strawberry.types import Info
import db.models as models
from src.resolvers import get_group, get_student_data


@strawberry.type
class Group:
    id: typing.Optional[int]
    name: str
    full_name: typing.Optional[str]

    @classmethod
    def marshal(cls, model: models.Group) -> "Group":
        return cls(
            id=strawberry.ID(str(model.id)),
            name=model.name,
            full_name=model.full_name
        )


@strawberry.type
class User:
    id: typing.Optional[int]
    surname: str
    name: str
    middle_name: typing.Optional[str]
    snils: typing.Optional[str]
    inn: typing.Optional[str]
    email: typing.Optional[str]
    phone: typing.Optional[str]
    study_year: int

    @strawberry.field
    async def student_data(self, info: Info) -> "StudentData":
        s_data = await get_student_data(info, self.id)
        return StudentData.marshal(s_data)

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
class StudentData:
    id: int
    group_id: int
    user_id: int
    degree_doc: str
    graduation_date: typing.Optional[date]

    @strawberry.field
    async def group(self, info: Info) -> "Group":
        student_group = await get_group(info, self.group_id)
        return Group.marshal(student_group)

    @classmethod
    def marshal(cls, model: models.StudentData) -> "StudentData":
        return cls(
            id=model.id,
            group_id=model.group_id,
            user_id=model.user_id,
            degree_doc=model.degree_doc,
            graduation_date=model.graduation_date
        )
