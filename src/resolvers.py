import typing

from sqlalchemy import select
from src.db.base import get_session
from src.db.models import Group, User, StudentData
from src.helper import get_valid_data
from loguru import logger


async def get_all_groups(info) -> typing.List[Group]:
    async with get_session() as session:
        query = select(Group).order_by(Group.name)
        result = (await session.execute(query)).scalars().all()
    return result


async def get_group(info, group_id: int) -> Group:
    async with get_session() as session:
        query = select(Group).where(Group.id == group_id)
        result = (await session.execute(query)).scalars().first()
        return result


async def add_group(name: str, full_name: str):
    async with get_session() as session:
        new_group = Group(name=name, full_name=full_name)
        session.add(new_group)
        await session.commit()
        return new_group


async def get_all_users(info) -> typing.List[User]:
    async with get_session() as session:
        query = select(User).order_by(User.name)
        result = (await session.execute(query)).scalars().all()
        return result


async def get_user(info, user_id: int) -> User:
    async with get_session() as session:
        query = select(User).where(User.id == user_id)
        result = (await session.execute(query)).scalars().first()
        return result


async def get_student_data(info, user_id: int) -> User:
    async with get_session() as session:
        query = select(StudentData).where(StudentData.user_id == user_id)
        result = (await session.execute(query)).scalars().first()
        return result


async def add_user(surname: str, name: str, middle_name: str, snils: str, inn: str,
                   email: str, phone: str, study_year: int) -> User:
    async with get_session() as session:
        new_user = User(surname=surname,
                        name=name,
                        middle_name=middle_name,
                        snils=snils,
                        inn=inn,
                        email=email,
                        phone=phone,
                        study_year=study_year
                        )
        session.add(new_user)
        await session.commit()
        return new_user