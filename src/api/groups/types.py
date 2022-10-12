import strawberry
from pydantic import typing

from db import models


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