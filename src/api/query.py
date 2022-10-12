import strawberry
from .users.query import UserQuery, AbsentQuery
from .groups.query import GroupQuery
from .student_data.query import StudentDataQuery


@strawberry.type
class Query(UserQuery, GroupQuery, StudentDataQuery, AbsentQuery):
    pass
