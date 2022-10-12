from pydantic import typing
from sqlalchemy import select

from db.base import get_session
from db.models import User, Group, StudentData, Absenteeism


async def get_users(group_id: int = None) -> typing.List[User]:
    if group_id:
        query = select(User).join(StudentData).where(StudentData.group_id == group_id)
    else:
        query = select(User).order_by(User.name)
    async with get_session() as session:
        result = (await session.execute(query)).scalars().all()
        return result


async def get_user(user_id: int) -> User:
    async with get_session() as session:
        query = select(User).where(User.id == user_id)
        result = (await session.execute(query)).scalars().first()
        return result


async def get_groups() -> typing.List[Group]:
    async with get_session() as session:
        query = select(Group).order_by(Group.name)
        result = (await session.execute(query)).scalars().all()
        return result


async def get_group(group_id: int) -> Group:
    async with get_session() as session:
        query = select(Group).where(Group.id == group_id)
        result = (await session.execute(query)).scalars().first()
        return result


async def get_student_data(user_id: int) -> StudentData:
    async with get_session() as session:
        query = select(StudentData).where(StudentData.user_id == user_id)
        result = (await session.execute(query)).scalars().first()
        return result


async def get_absents(user_id: int) -> typing.List[Absenteeism]:
    async with get_session() as session:
        query = select(Absenteeism).where(Absenteeism.user_id == user_id)
        result = (await session.execute(query)).scalars().all()
        return result
