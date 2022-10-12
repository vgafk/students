import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig

from api.query import Query
# from db.models import init_models
# import asyncio


app = FastAPI()

schema = strawberry.Schema(query=Query, #mutation=Mutation,
                           config=StrawberryConfig(auto_camel_case=False))

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")