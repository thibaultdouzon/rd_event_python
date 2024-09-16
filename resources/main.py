import time
from contextlib import contextmanager
from typing import Any, Generator, Generic, Optional, TypeVar

from fastapi import FastAPI
from loguru import logger
from pydantic import BaseModel

app = FastAPI()

# Some generic type
T = TypeVar("T")


class User(BaseModel):
    id: int
    name: str


class Response(BaseModel, Generic[T]):
    code: int
    message: str
    data: Optional[T] = None


database = [User(id=id, name=name) for id, name in enumerate(["Alice", "Bob", "Eve"])]


@contextmanager
def measure_time() -> Generator[None, Any, None]:
    start_time = time.perf_counter_ns()
    yield
    end_time = time.perf_counter_ns()
    logger.info(f"Execution time: {end_time - start_time:.2f} nano seconds")


@app.get("/")
async def index() -> Response[None]:
    return Response[None](code=200, message="Hello, World!")


@app.get("/user/{id:int}")
async def get_user(id: int) -> Response[User]:
    logger.info(f"Getting user with {id = }")
    try:
        with measure_time():
            index = [user.id for user in database].index(id)
            user = database[index]

        return Response[User](code=200, message="User found", data=user)
    except ValueError:
        logger.error(f"User with {id = } not found")
        return Response[User](code=404, message="User not found")


@app.post("/user")
async def create_user(user: User) -> Response[User]:
    logger.info(f"Appending {user = }")
    if user.id not in (user.id for user in database):
        database.append(user)
        return Response[User](code=201, message="User created", data=user)

    return Response[User](code=400, message="User already exists")
