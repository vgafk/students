import strawberry
from .types import StudentData
from db.query_resolvers import get_student_data


@strawberry.type
class StudentDataQuery:

    @strawberry.field
    async def student_data(self, user_id: int) -> StudentData:
        data = await get_student_data(user_id)
        return StudentData.marshal(data)