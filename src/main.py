import strawberry
import uvicorn
from fastapi import FastAPI
from loguru import logger
from strawberry.fastapi import GraphQLRouter
from src.schema import Query, Mutation

import settings

application = FastAPI()
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)
application.include_router(graphql_app, prefix="/graphql")

if __name__ == '__main__':
    logger.info('Старт скрипта')
    logger.info('Старт сервера')
    uvicorn.run("main:application",
                host=settings.HOST,
                port=settings.PORT,
                reload=True)

