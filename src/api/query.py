import strawberry
from .users.query import UserQuery
from .groups.query import GroupQuery
from .student_data.query import StudentDataQuery
from api.absents.query import AbsentQuery


@strawberry.type
class Query(UserQuery, GroupQuery, StudentDataQuery, AbsentQuery):
    pass
