from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main():
    return "Главная страница"


@app.get("/user/admin")
async def admin():
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def user_id(user_id: int):
    return f"Вы вошли как пользователь №{user_id}"


@app.get("/user")
async def user_info(username: str = 'Andrey', age: int = 24):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
