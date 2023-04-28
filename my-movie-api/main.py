from fastapi import FastAPI
from config.database import  engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router

app = FastAPI()
app.title = "My movie app"
app.version = 1.0

# Incluir Middlewares
app.add_middleware(ErrorHandler)
# Incluir Roter
app.include_router(movie_router)
# Creacion y conexion base de datos
Base.metadata.create_all(bind=engine)





'''
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
        "id": 1,
        "title": "Mi pelicula",
        "overview": "Descripcion de la pelicula",
        "year": 2022,
        "rating": 9.8,
        "category": "Accion"
    },
    {
        "id": 2,
        "title": "Mi pelicula2",
        "overview": "Descripcion de la pelicula2",
        "year": 2022,
        "rating": 9.8,
        "category": "Accion2"
    },
    {
        "id": 3,
        "title": "Mi pelicula3",
        "overview": "Descripcion de la pelicula3",
        "year": 2023,
        "rating": 9.5,
        "category": "Accion3"
    }
]

 Rutas extra para entender el funcionamiento del aplicativo
@app.get("/movies",status_code=200,dependencies=[Depends(JWTBearer)])
def find_all_movies():
    return JSONResponse(status_code=200, content=movies)

@app.get("/movies/",tags=["movies"])
def get_movies_by_category(categories: str = Query(min_length=5)):
     return list(filter(lambda movie : movie["category"] == categories, movies))
'''

