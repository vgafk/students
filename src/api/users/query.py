from datetime import datetime

import strawberry
from pydantic import typing

from .types import User, Absents
from db.resolvers import get_users, get_user, get_absents


@strawberry.type
class UserQuery:

    @strawberry.field
    async def users(self, group_id: int = None) -> typing.List[User]:
        all_users = await get_users(group_id)
        return [User.marshal(user) for user in all_users]

    @strawberry.field
    async def user(self, user_id: int) -> User:
        user = await get_user(user_id)
        return User.marshal(user)


@strawberry.type
class AbsentQuery:

    @strawberry.field
    async def absent(self, user_id: int) -> typing.List[Absents]:
        absents = await get_absents(user_id)
        return [Absents.marshal(absent) for absent in absents]
