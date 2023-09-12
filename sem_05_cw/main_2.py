# Задание No2
# 📌 Создать API для получения списка фильмов по жанру.
#    Приложение должно иметь возможность получать список фильмов по заданному жанру.
# 📌 Создайте модуль приложения и настройте сервер и маршрутизацию.
# 📌 Создайте класс Movie с полями id, title, description и genre.
# 📌 Создайте список movies для хранения фильмов.
# 📌 Создайте маршрут для получения списка фильмов по жанру (метод GET).
# 📌 Реализуйте валидацию данных запроса и ответа.

from enum import Enum
from typing import Optional
from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

app = FastAPI()


class Genre(Enum):
    horror = 'ужас'
    fantasy = 'фэнтези'
    comedy = 'комедия'
    action = 'боевик'


class Movie(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    genre: Genre


class MovieIn(BaseModel):
    title: str
    description: Optional[str] = None
    genre: Genre


movies = []


@app.get("/movies/{genre}", response_model=list[Movie])
async def get_movies_by_genre(genre: Genre):
    return list(filter(lambda movie: movie.genre == genre, movies))


@app.post("/movies/", response_model=Movie)
async def add_movies(movie: MovieIn):
    new_movie = Movie(id=len(movies) + 1, title=movie.title, description=movie.description, genre=movie.genre)
    movies.append(new_movie)
    return new_movie


if __name__ == '__main__':
    uvicorn.run(
        "main_2:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
