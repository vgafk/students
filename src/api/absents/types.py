import datetime
import strawberry
from pydantic import types

from db import models


@strawberry.type
class Absents:
    id: int
    date: datetime.date
    class_number: int

    @classmethod
    def marshal(cls, data: types.Dict[str, str]) -> "Absents":
        return cls(
            id=data['id'],
            date=datetime.date.fromisoformat(data['date']),
            class_number=data['class_number']
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

