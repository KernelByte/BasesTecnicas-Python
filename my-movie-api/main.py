from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
import Esquemas
from jwt_manager import create_token

app = FastAPI()
app.title = "My movie app"
app.version = 1.0


@app.get("/", tags=["Home url"], response_class=HTMLResponse)
def get_message():
    return "<h1>Hello world</h1>"


@app.get("/person", tags=["Person url"])
def get_person():
    return [
        {
            "name": "Yoniher Melendez",
            "age": 23
        },

        {
            "name": "Oscar Martinez",
            "age": 34
        }
    ]


# Lista de peliculas
movies = [
    {
        "id" : 1,
        "name": "Spiderman",
        "category": "Super hero"
    },
    {
        "id" : 2,
        "name": "Acuaman",
        "category": "Super hero"
    },
    {
        "id" : 3,
        "name": "Superman",
        "category": "Super hero"
    },
    {
        "id" : 4,
        "name": "JonWhit",
        "category": "Action"
    }
]

@app.get("/movies",status_code=200)
def find_all_movies():
    return JSONResponse(status_code=200, content=movies)

@app.get("/movies/{id}",tags=["movies"])
def get_movies(id: int = Path(ge=1, le=200)):
     return list(filter(lambda movie : movie["id"] == id, movies))


@app.get("/movies/",tags=["movies"])
def get_movies_by_category(categories: str = Query(min_length=5)):
     return list(filter(lambda movie : movie["category"] == categories, movies))

# Metodo POST
@app.post("/movies",tags=["movies"], status_code=201)
def create_movie(movie : Esquemas.Movie):
     movies.append(movie)
     return movies

# Metodo PUT
@app.put("/movies/{id}", tags=["movies"])
def update_movies(id: int, movie : Esquemas.Movie):
     for item in movies:
          if item["id"] == id:
               item["name"] = movie.name
               item["category"] = movie.category
     return JSONResponse(content={"message": "Se a modificado la pelicula"})

# Metodo DELETE
@app.delete("/movies/{id}", tags=["movies"])
def delete_movie(id: int):
     for item in movies:
          if item["id"] == id:
               movies.remove(item)
     return movies


@app.post("/login", tags=["Login"])
def login(user: Esquemas.User):
     return user