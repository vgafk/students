from typing import Optional
from pydantic import BaseModel


class StudentSchema(BaseModel):
    id: Optional[int]
    surname: str
    name: str
    middle_name: Optional[str]
    snils: Optional[str]
    inn: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    study_year: int
