import strawberry
from pydantic import typing
from strawberry.types import Info

from scalars import Group, User, StudentData
import resolvers


@strawberry.type
class Query:

    @strawberry.field
    async def groups(self, info: Info) -> typing.List[Group]:
        groups = await resolvers.get_all_groups(info)
        return [Group.marshal(group) for group in groups]

    @strawberry.field
    async def group(self, info: Info, group_id: int) -> Group:
        group = await resolvers.get_group(info, group_id)
        return Group.marshal(group)

    @strawberry.field
    async def users(self, info: Info) -> typing.List[User]:
        users = await resolvers.get_all_users(info)
        return [User.marshal(user) for user in users]

    @strawberry.field
    async def user(self, info: Info, user_id: int) -> User:
        user = await resolvers.get_user(info, user_id)
        return User.marshal(user)

    @strawberry.field
    async def student_data(self, info: Info, user_id: int) -> StudentData:
        student_data = await resolvers.get_student_data(info, user_id)
        return StudentData.marshal(student_data)


@strawberry.type
class Mutation:

    @strawberry.mutation
    async def add_group(self, name: str, full_name: str) -> Group:
        add_group_resp = await resolvers.add_group(name, full_name)
        return add_group_resp

    @strawberry.mutation
    async def add_user(self, surname: str, name: str, middle_name: str, snils: str, inn: str,
                       email: str, phone: str, study_year: int) -> User:
        add_user_resp = await resolvers.add_user(surname, name, middle_name, snils, inn, email, phone, study_year)
        return add_user_resp
