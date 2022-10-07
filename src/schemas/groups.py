from typing import Optional
from pydantic import BaseModel


class GroupSchema(BaseModel):
    id: Optional[int]
    name: str
    full_name: str
