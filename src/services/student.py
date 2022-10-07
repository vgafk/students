from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Group


def add_group(session: AsyncSession, name: str, full_name: str):
    new_group = Group(name=name, full_name=full_name)
    session.add(new_group)
    return new_group


async def get_all_groups(session: AsyncSession) -> list[Group]:
    result = await session.execute(select(Group).order_by(Group.name))
    return result.scalars().all()


async def get_group(group_id: int, session: AsyncSession) -> Group:
    result = await session.execute(select(Group).where(Group.id == group_id))
    return result.scalars().first()