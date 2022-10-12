import strawberry
from pydantic import typing
from pydantic.types import date

from db import models
from api.groups.query import GroupQuery, Group


@strawberry.type
class StudentData:
    id: int
    group_id: int
    user_id: int
    degree_doc: str
    graduation_date: typing.Optional[date]

    @strawberry.field
    async def group(self) -> Group:
        return await GroupQuery().group(self.group_id)

    @classmethod
    def marshal(cls, model: models.StudentData) -> "StudentData":
        return cls(
            id=model.id,
            group_id=model.group_id,
            user_id=model.user_id,
            degree_doc=model.degree_doc,
            graduation_date=model.graduation_date
        )
