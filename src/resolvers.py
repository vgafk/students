import typing

from sqlalchemy import select
from src.db.base import get_session
from src.db.models import Group, User
from src.helper import get_valid_data


async def get_all_groups(info) -> typing.List[Group]:
    async with get_session() as session:
        query = select(Group).order_by(Group.name)
        result = (await session.execute(query)).scalars().all()

    groups_data_list = []

    for group in result:
        group_dict = get_valid_data(group, Group)
        groups_data_list.append(Group(**group_dict))

    return groups_data_list


async def get_group(info, group_id: int) -> Group:
    async with get_session() as session:
        query = select(Group).where(Group.id == group_id)
        result = (await session.execute(query)).scalars().first()
        group_dict = get_valid_data(result, Group)
        group = Group(**group_dict)
        return group


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

    user_data_list = []

    for user in result:
        user_dict = get_valid_data(user, User)
        user_data_list.append(User(**user_dict))

    return user_data_list


async def get_user(info, user_id: int) -> User:
    async with get_session() as session:
        query = select(User).where(User.id == user_id)
        result = (await session.execute(query)).scalars().first()
        user_dict = get_valid_data(result, User)
        user = User(**user_dict)
        return user


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
