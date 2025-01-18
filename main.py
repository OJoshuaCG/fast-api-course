from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse


app = FastAPI()

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "Es un exuberante planeta llamado Pandora viven los Na'vi",
        "year": "2009",
        "rating": 7.8,
        "category": "Accion",
    },
    {
        "id": 2,
        "title": "Avatar",
        "overview": "Es un exuberante planeta llamado Pandora viven los Na'vi",
        "year": "2005",
        "rating": 8.2,
        "category": "Comedia",
    },
]


@app.get("/", tags=["Home"])
def home():
    return {"Hello": "World"}


@app.get("/movies", tags=["Movies"])
def get_movies():
    # return {"Hello": "World"}
    # return HTMLResponse("<h1>Hello world!</h1>")
    return movies


# Parametros de ruta
# El valor se incluye en la URL, despues de una diagonal /2
@app.get("/movies/{id}", tags=["Movies"])
def get_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            return movie
    return []


# Parametros query
# El valor se define con una clave dentro de la URL, id=1
@app.get("/movies/", tags=["Movies"])
def get_movie_by_category(category: str, year: int):
    # return category
    # return year
    for movie in movies:
        if movie["category"] == category:
            return movie
    return []


@app.post("/movies", tags=["Movies"])
def create_movies(
    id: int = Body(),
    title: str = Body(),
    overview: str = Body(),
    year: int = Body(),
    rating: float = Body(),
    category: str = Body(),
):
    movies.append(
        {
            "id": id,
            "title": title,
            "overview": overview,
            "year": year,
            "rating": rating,
            "category": category,
        }
    )
    return movies


@app.put("/movies/{id}", tags=["Movies"])
def update_movie(
    id: int,
    title: str = Body(),
    overview: str = Body(),
    year: int = Body(),
    rating: float = Body(),
    category: str = Body(),
):
    for movie in movies:
        if movie["id"] == id:
            movie["title"] = title
            movie["overview"] = overview
            movie["year"] = year
            movie["rating"] = rating
            movie["category"] = category
    return movies


@app.delete("/movies/{id}", tags=["Movies"])
def delete_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
    return movies
