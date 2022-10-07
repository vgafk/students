import strawberry
from pydantic import typing


@strawberry.type
class Group:
    id: typing.Optional[int]
    name: str
    full_name: typing.Optional[str]


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
