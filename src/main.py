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
async def create_user(user):
    if user.id not in (user["id"] for user in database):
        database.append(user)
        return user

    return None
