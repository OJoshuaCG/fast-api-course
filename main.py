from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Optional, List
import datetime

app = FastAPI()


class Movie(BaseModel):
    # id: int
    # id: int | None = None
    id: Optional[int] = None
    title: str
    overview: str
    year: int
    rating: float
    category: str


class MovieCreate(BaseModel):
    id: int
    title: str = Field(min_length=5, max_length=15)  # , default="My movie")
    overview: str = Field(
        min_length=15, max_length=50
    )  # , default="Esta pelicula trata acerca de...")
    year: int = Field(le=datetime.date.today().year, ge=1900)  # , default=2022)
    rating: float = Field(ge=0, le=10)  # , default=10)
    category: str = Field(min_length=5, max_digits=20)  # , default="Accion")

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "title": "My Movie",
                "overview": "Esta pelicula trata acerca de...",
                "year": 2022,
                "rating": 5,
                "category": "Comedia",
            }
        }
    }


class MovieUpdate(BaseModel):
    title: str
    overview: str
    year: int
    rating: float
    category: str


movies: list[Movie] = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "Es un exuberante planeta llamado Pandora viven los Na'vi",
        "year": 2009,
        "rating": 7.8,
        "category": "Accion",
    },
    {
        "id": 2,
        "title": "Avatar",
        "overview": "Es un exuberante planeta llamado Pandora viven los Na'vi",
        "year": 2005,
        "rating": 8.2,
        "category": "Comedia",
    },
]


@app.get("/", tags=["Home"])
def home():
    return {"Hello": "World"}


@app.get("/movies", tags=["Movies"])
def get_movies() -> list[Movie]:
    # return {"Hello": "World"}
    # return HTMLResponse("<h1>Hello world!</h1>")
    return movies


# Parametros de ruta
# El valor se incluye en la URL, despues de una diagonal /2
@app.get("/movies/{id}", tags=["Movies"])
def get_movie(id: int) -> Movie:
    for movie in movies:
        if movie["id"] == id:
            return movie
    return []


# Parametros query
# El valor se define con una clave dentro de la URL, id=1
@app.get("/movies/", tags=["Movies"])
def get_movie_by_category(category: str, year: int) -> Movie:
    # return category
    # return year
    for movie in movies:
        if movie["category"] == category:
            return movie
    return []


@app.post("/movies", tags=["Movies"])
def create_movie(movie: MovieCreate) -> list[Movie]:
    movies.append(movie.model_dump())
    return movies


@app.put("/movies/{id}", tags=["Movies"])
def update_movie(id: int, movie: MovieUpdate) -> list[Movie]:
    for item in movies:
        if item["id"] == id:
            item["title"] = movie.title
            item["overview"] = movie.overview
            item["year"] = movie.year
            item["rating"] = movie.rating
            item["category"] = movie.category
    return movies


@app.delete("/movies/{id}", tags=["Movies"])
def delete_movie(id: int) -> list[Movie]:
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
    return movies
