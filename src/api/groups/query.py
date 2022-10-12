import strawberry
from pydantic import typing

from .types import Group
from db.query_resolvers import get_groups, get_group


@strawberry.type
class GroupQuery:

    @strawberry.field
    async def groups(self, faculty_id: typing.Optional[int] = None) -> typing.Optional[typing.List[Group]]:
        all_groups = await get_groups(faculty_id)
        return [Group.marshal(group) for group in all_groups]

    @strawberry.field
    async def group(self, group_id: int) -> Group:
        group = await get_group(group_id)
        return Group.marshal(group)
