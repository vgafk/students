import strawberry
from pydantic import typing
from strawberry.types import Info

from scalars import Group, User
from resolvers import get_all_groups, get_group, add_group, get_all_users, get_user, add_user


@strawberry.type
class Query:

    @strawberry.field
    async def groups(self, info: Info) -> typing.List[Group]:
        groups_data_list = await get_all_groups(info)
        return groups_data_list

    @strawberry.field
    async def group(self, info: Info, group_id: int) -> Group:
        groups_data = await get_group(info, group_id)
        return groups_data

    @strawberry.field
    async def users(self, info: Info) -> typing.List[User]:
        users_data_list = await get_all_users(info)
        return users_data_list

    @strawberry.field
    async def user(self, info: Info, user_id: int) -> User:
        user_data = await get_user(info, user_id)
        return user_data


@strawberry.type
class Mutation:

    @strawberry.mutation
    async def add_group(self, name: str, full_name: str) -> Group:
        add_group_resp = await add_group(name, full_name)
        return add_group_resp

    @strawberry.mutation
    async def add_user(self, surname: str, name: str, middle_name: str, snils: str, inn: str,
                       email: str, phone: str, study_year: int) -> User:
        add_user_resp = await add_user(surname, name, middle_name, snils, inn, email, phone, study_year)
        return add_user_resp
