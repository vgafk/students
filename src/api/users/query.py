import strawberry
from pydantic import typing

from .types import User
from db.query_resolvers import get_users, get_user


@strawberry.type
class UserQuery:

    @strawberry.field
    async def users(self, group_id: typing.Optional[int] = None) -> typing.List[User]:
        all_users = await get_users(group_id)
        return [User.marshal(user) for user in all_users]

    @strawberry.field
    async def user(self, user_id: int) -> User:
        user = await get_user(user_id)
        return User.marshal(user)
