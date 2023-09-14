# Задание No1 (продолжение)
# 📌 API должно поддерживать следующие операции:
#    ○ Получение списка всех пользователей: GET /users/
#    ○ Получение информации о конкретном пользователе: GET /users/{user_id}/
#    ○ Создание нового пользователя: POST /users/
#    ○ Обновление информации о пользователе: PUT /users/{user_id}/
#    ○ Удаление пользователя: DELETE /users/{user_id}/
# 📌 Для валидации данных используйте параметры Field модели User.
# 📌 Для работы с базой данных используйте SQLAlchemy и модуль databases.

import uvicorn
from fastapi import FastAPI
from db import database
from routers import user

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(user.router, tags=["users"])

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
