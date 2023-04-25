from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

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

@app.get("/movies/{id}",tags=["movies"])
def get_movies(id: int):
     return list(filter(lambda movie : movie["id"] == id, movies))


@app.get("/movies/",tags=["movies"])
def get_movies_by_category(categories: str):
     return list(filter(lambda movie : movie["category"] == categories, movies))

# Metodo POST
@app.post("/movies",tags=["movies"])
def create_movie(id: int = Body(),name: str = Body(),category: str = Body()):
     movies.append({
        "id" : id,
        "name": name,
        "category": category
     })
     return movies