import asyncio
import typer
from fastapi import FastAPI
from db.base import init_models
from routers import groups

app = FastAPI()
cli = typer.Typer()


@cli.command()
def db_init_models():
    asyncio.run(init_models())
    print("Done")


app.include_router(groups.router)


@app.api_route("/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def only_api():
    return {'Error': 'Работа с сервером осуществляется только через API, обратитесь к документации /docs'}


if __name__ == "__main__":
    cli()


# REST версия