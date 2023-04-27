# Metodo para la creacion de esquema de datos
from pydantic import BaseModel, Field

class Movie(BaseModel):
    id: int | None = None
    name: str = Field(default="Ingresa nombre", max_length=2000)
    category: str = Field(default="Ingresa la categoria")

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Oscar Martinez",
                "category": "Action"
            }
        }

class User(BaseModel):
    email:str
    password:str