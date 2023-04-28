# Metodo para la creacion de esquema de datos
from pydantic import BaseModel, Field

class User(BaseModel):
    email:str
    password:str