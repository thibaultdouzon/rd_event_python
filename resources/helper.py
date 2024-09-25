from typing import Any

import requests

url = "http://localhost:8000/"


def get_user(id: int) -> Any:
    response = requests.get(f"{url}user/{id}").json()
    return response


def insert_user(id: int, name: str) -> Any:
    user = {"id": id, "name": name}
    response = requests.post(f"{url}user", json=user).json()
    return response


def insert_user_additional_field(id: int, name: str, **kwargs: Any) -> Any:
    user = {"id": id, "name": name, **kwargs}
    response = requests.post(f"{url}user", json=user).json()
    return response
