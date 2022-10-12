from typing import Dict, Any

from sqlalchemy.dialects.sqlite import insert
from sqlalchemy.exc import IntegrityError
from loguru import logger

from .base import get_session
from .models import Group, User, StudentData


async def add_group(group: Dict[str, str]) -> Any:
    async with get_session() as session:
        try:
            new_group = {
                'name': group['name'],
                'full_name': group.get('full_name'),
                'faculty_id': int(group['faculty_id'])
            }
            query = insert(Group).values(new_group)
            await session.execute(query)
            await session.commit()
        except IntegrityError:
            pass


async def add_student(student: Dict[str, str]) -> Any:
    async with get_session() as session:
        try:
            new_user = {
                'surname': student['surname'],
                'name': student['name'],
                'middle_name': student['middle_name'],
                'snils': student['snils'],
                'inn': student['inn'],
                'email': student['email'],
                'phone': student['phone'],
                'study_year': int(student['study_year'])
            }
            query = insert(User).values(new_user)
            user_id = (await session.execute(query)).lastrowid

            new_student_data = {
                'user_id': user_id,
                'group_id': student['group_id'],
            }
            query_data = insert(StudentData).values(new_student_data)
            await session.execute(query_data)

            await session.commit()

        except IntegrityError:
            session.rollback()
