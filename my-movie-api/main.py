from fastapi import FastAPI, Body, Path, Query, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.security import HTTPBearer
from fastapi.encoders import jsonable_encoder
import Esquemas
from jwt_manager import create_token, validate_token
from config.database import Session, engine, Base
from models.movie import Movie as MovieModel

app = FastAPI()
app.title = "My movie app"
app.version = 1.0

# Creacion y conexion base de datos
Base.metadata.create_all(bind=engine)


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        respuesta = await super().__call__(request)
        data = validate_token(respuesta.credentials)
        if data["email"] != "admin@gmail.com":
            raise HTTPException(
                status_code=403, detail="Las credenciales son invalidas")


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

''' Rutas extra para entender el funcionamiento del aplicativo
@app.get("/movies",status_code=200,dependencies=[Depends(JWTBearer)])
def find_all_movies():
    return JSONResponse(status_code=200, content=movies)

@app.get("/movies/",tags=["movies"])
def get_movies_by_category(categories: str = Query(min_length=5)):
     return list(filter(lambda movie : movie["category"] == categories, movies))
'''


@app.get("/movies", tags=["movies"], response_model=list[Esquemas.Movie], status_code=200)
def get_all_movies() -> list[Esquemas.Movie]:
    db = Session()
    result = db.query(MovieModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@app.get("/movies/{id}", tags=["movies"], dependencies=[Depends(JWTBearer)])
def get_movies(id: int = Path(ge=1, le=200)):
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "Movie no encontrada"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Metodo POST


@app.post("/movies", tags=["movies"], status_code=201)
def create_movie(movie: Esquemas.Movie) -> dict:
    db = Session()
    new_movie = MovieModel(**movie.dict())
    db.add(new_movie)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la pelicula de manera correcta"})

# Metodo PUT


@app.put("/movies/{id}", tags=["movies"])
def update_movies(id: int, movie: Esquemas.Movie):
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

# EndPoint de LOGIN


@app.post("/login", tags=["Login"])
def login(user: Esquemas.User):

    if user.email == "admin@gmail.com" and user.password == "12345":
        token: str = create_token(user.dict())
    return JSONResponse(status_code=200, content=token)

    return user
