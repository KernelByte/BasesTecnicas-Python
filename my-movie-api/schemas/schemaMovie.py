# Metodo para la creacion de esquema de datos
from pydantic import BaseModel, Field

class Movie(BaseModel):
    id: int | None = None
    title: str = Field(default="Ingresa un titulo", max_length=2000)
    overview: str = Field(default="Ingresa el overview")
    year: int 
    rating: float 
    category: str 

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi pelicula",
                "overview": "Descripcion de la pelicula",
                "year": 2022,
                "rating": 9.8,
                "category": "Accion"
            }
        }