# Metodo para la creacion de esquema de datos
from pydantic import BaseModel

class Movie(BaseModel):
    id: int | None = None
    name: str 
    category: str