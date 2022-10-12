import os

from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from typing import Dict
from csv import DictReader

from db.mutations_resolvers import add_group, add_student
from server_loger import add_to_log

file_router = APIRouter()


@file_router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    new_file_name = file.filename
    with open(new_file_name, 'wb') as new_file:
        new_file.write(content)

    await handle_file(new_file_name)

    return JSONResponse('Uploaded', status_code=200)


async def handle_file(file: str):
    function = None
    match file:
        case 'groups.csv':
            function = add_group
        case 'students.csv':
            function = add_student
        case _:
            add_to_log(f'{file}')

    if function:
        with open(file, 'r') as open_file:
            data = DictReader(open_file, dialect='excel')
            for row in data:
                await function(row)

    os.remove(file)
