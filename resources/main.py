from dataclasses import dataclass
from typing import TypedDict


class UserDict(TypedDict):
    name: str
    age: int


@dataclass
class User:
    name: str
    age: int


def get_age(user: User | UserDict) -> int:
    if isinstance(user, User):
        return user.age
    elif isinstance(user, dict):
        return user["age"]


def add(a: int, b: int) -> int:
    return a + b


def main() -> None:
    u: UserDict = {
        "name": "doudou",
        "age": 10,
    }
    print(get_age(u))


if __name__ == "__main__":
    main()
