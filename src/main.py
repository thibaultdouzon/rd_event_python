import time
from contextlib import contextmanager
from typing import Any, Generator, Generic, Optional, TypeVar

from fastapi import FastAPI
from loguru import logger
from pydantic import BaseModel

logger.add("app.log", level="INFO")

app = FastAPI()

# Some generic type
T = TypeVar("T")


class User(BaseModel):
    id: int
    name: str


class Response(BaseModel, Generic[T]):
    code: int
    message: str
    data: Optional[T]


database = [
    User(id=1, name="John Doe"),
    User(id=2, name="Alice"),
    User(id=3, name="Bob"),
]


@contextmanager
def measure_time() -> Generator[None, Any, None]:
    start_time = time.perf_counter_ns()
    yield
    end_time = time.perf_counter_ns()
    logger.info(f"Execution time: {end_time - start_time:.2f} nano seconds")


@app.get("/")
async def index() -> Response[None]:
    return Response[None](code=200, message="Hello, World!", data=None)


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
        return Response[User](code=404, message="User not found", data=None)


@app.post("/user")
async def create_user(user: User) -> Response[User]:
    logger.info(f"Appending {user = }")
    if user.id not in [user.id for user in database]:
        database.append(user)
        return Response[User](code=201, message="User created", data=user)

    return Response[User](code=400, message="User already exists", data=None)
