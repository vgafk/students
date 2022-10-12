import asyncio

import requests
from pydantic import typing
from python_graphql_client import GraphqlClient
from api.exceptions import AbsentConnectionError

END_POINT = "http://127.0.0.1:11801/graphql"


def get_absents(user_id: int) -> typing.List[typing.Dict[str, str]]:
    client = GraphqlClient(endpoint=END_POINT, verify=False)
    query = """
        query absent_query($user_id: Int!){
            absent(user_id: $user_id){
                id, date, class_number
                }
            }
    """
    variables = {"user_id": user_id}
    try:
        data = client.execute(query=query, variables=variables)
        answer = data['data']['absent']
        return answer
    except requests.exceptions.ConnectionError:
        raise AbsentConnectionError('Сервис пропусков занятий не доступен')
