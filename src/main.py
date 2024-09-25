from fastapi import FastAPI

app = FastAPI()


database = [{"id": id, "name": name} for id, name in enumerate(["Alice", "Bob", "Eve"])]


@app.get("/")
async def index():
    return "Hello, World!"


@app.get("/user/{id:int}")
async def get_user(id):
    try:
        index = [user["id"] for user in database].index(id)
        user = database[index]
        return user

    except ValueError:
        return None


@app.post("/user")
async def create_user(new_user):
    if new_user["id"] not in (user["id"] for user in database):
        database.append(new_user)
        return new_user

    return None
