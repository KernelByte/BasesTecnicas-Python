from fastapi import APIRouter
import Esquemas
from fastapi import  Path, Depends
from fastapi.responses import  JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session
from models.movie import Movie as MovieModel
from middlewares.jwt_bearer import JWTBearer
from services.movieService import MovieService

movie_router = APIRouter()

# Metodo GET - TODOS LOS REGISTROS
@movie_router.get("/movies", tags=["movies"], response_model=list[Esquemas.Movie], status_code=200)
def get_all_movies() -> list[Esquemas.Movie]:
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
def create_movie(movie: Esquemas.Movie) -> dict:
    db = Session()
    new_movie = MovieModel(**movie.dict())
    db.add(new_movie)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la pelicula de manera correcta"})



# Metodo PUT
@movie_router.put("/movies/{id}", tags=["movies"])
def update_movies(id: int, movie: Esquemas.Movie) -> dict:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "Movie no encontrada"})
    result.title = movie.title
    result.overview = movie.overview
    result.year =  movie.year
    result.rating = movie.rating
    result.category = movie.category
    db.commit()
    return JSONResponse(content={"message": "Se a modificado la pelicula"})



# Metodo DELETE
@movie_router.delete("/movies/{id}", tags=["movies"])
def delete_movie(id: int) -> dict:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "Movie no encontrada"})
    else:
       db.delete(result)
       db.commit()
       return JSONResponse(content={"message": "Se a eliminado la pelicula"})
