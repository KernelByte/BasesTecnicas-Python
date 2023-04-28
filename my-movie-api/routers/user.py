from fastapi import APIRouter
import Esquemas
from jwt_manager import create_token
from fastapi.responses import  JSONResponse

user_router = APIRouter()

# EndPoint de LOGIN
@user_router.post("/login", tags=["Login"])
def login(user: Esquemas.User):

    if user.email == "admin@gmail.com" and user.password == "12345":
        token: str = create_token(user.dict())
    return JSONResponse(status_code=200, content=token)

    return user