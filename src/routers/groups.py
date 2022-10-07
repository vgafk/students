from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from schemas.groups import GroupSchema
import services.groups as service
from db.base import get_session
from exceptions import DuplicatedEntryError

router = APIRouter()


@router.post("/groups")
async def add_group(group: GroupSchema, session: AsyncSession = Depends(get_session)):
    group = service.add_group(session, group.name, group.full_name)
    try:
        await session.commit()
        return group
    except IntegrityError as ex:
        await session.rollback()
        raise DuplicatedEntryError("Такая группа уже есть в базе")


@router.get("/groups")
async def get_all_groups(session: AsyncSession = Depends(get_session)):
    groups = await service.get_all_groups(session)
    return {'groups': [GroupSchema(id=group.id,
                                   name=group.name,
                                   full_name=group.full_name)
            for group in groups]}


@router.get("/groups/{group_id}")
async def get_group(group_id: int, session: AsyncSession = Depends(get_session)):
    group = await service.get_group(group_id, session)
    return {'group': GroupSchema(id=group.id, name=group.name, full_name=group.full_name)}