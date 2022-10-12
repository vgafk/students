import strawberry
from pydantic import typing

from db import models


@strawberry.type
class Group:
    id: typing.Optional[int]
    name: str
    full_name: typing.Optional[str]
    faculty_id: int

    @classmethod
    def marshal(cls, model: models.Group) -> "Group":
        return cls(
            id=model.id,
            name=model.name,
            full_name=model.full_name,
            faculty_id=model.faculty_id
        )