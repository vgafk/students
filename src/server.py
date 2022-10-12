import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig

from api.query import Query
from db import init_models
from files import file_router
import asyncio


app = FastAPI()

schema = strawberry.Schema(query=Query, #mutation=Mutation,
                           config=StrawberryConfig(auto_camel_case=False))

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")
app.include_router(file_router, prefix="/files")


if __name__ == '__main__':
    asyncio.run(init_models())