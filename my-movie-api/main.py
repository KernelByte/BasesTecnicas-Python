from fastapi import FastAPI
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
    }
]

@app.get("/movies/{id}")
def get_movies(id: int):
     return list(filter(lambda movie : movie["id"] == id, movies))