import requests

from src.main import Response, User

url = "http://localhost:8000/"


def get_user(id: int) -> Response[User]:
    response = requests.get(f"{url}user/{id}").json()
    return Response[User](**response)


def insert_user(id: int, name: str) -> Response[User]:
    user = User(id=id, name=name)
    response = requests.post(f"{url}user", json=user.model_dump()).json()
    return Response[User](**response)
