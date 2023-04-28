from fastapi import APIRouter
from schemas.schemaMovie import Movie
from fastapi import  Path, Depends
from fastapi.responses import  JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session
from models.movie import Movie as MovieModel
from middlewares.jwt_bearer import JWTBearer
from services.movieService import MovieService

movie_router = APIRouter()

# Metodo GET - TODOS LOS REGISTROS
@movie_router.get("/movies", tags=["movies"], response_model=list[Movie], status_code=200)
def get_all_movies() -> list[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))



# Metodo GET - UN SOLO REGISTRO
@movie_router.get("/movies/{id}", tags=["movies"], dependencies=[Depends(JWTBearer)])
def get_movies(id: int = Path(ge=1, le=200)):
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Movie no encontrada"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))



# Metodo POST
@movie_router.post("/movies", tags=["movies"], status_code=201)
def create_movie(movie: Movie) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la pelicula de manera correcta"})



# Metodo PUT
@movie_router.put("/movies/{id}", tags=["movies"])
def update_movies(id: int, movie: Movie) -> dict:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Movie no encontrada"})
    MovieService(db).update_movie(id, movie)
    return JSONResponse(content={"message": "Se a modificado la pelicula"})



# Metodo DELETE
@movie_router.delete("/movies/{id}", tags=["movies"])
def delete_movie(id: int) -> dict:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Movie no encontrada"})
    else:
       MovieService(db).delete_movie(id)
       return JSONResponse(content={"message": "Se a eliminado la pelicula"})
