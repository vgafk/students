import strawberry
from typing import Optional, List

from .types import Absents
from .resolvers import get_absents
from api.exceptions import AbsentConnectionError


@strawberry.type
class AbsentQuery:

    @strawberry.field
    def absent(self, user_id: int) -> Optional[List[Absents]]:
        try:
            absents = get_absents(user_id)
            return [Absents.marshal(absent) for absent in absents]
        except AbsentConnectionError:
            pass
