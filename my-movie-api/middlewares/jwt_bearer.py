from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from utils.jwt_manager import validate_token

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        respuesta = await super().__call__(request)
        data = validate_token(respuesta.credentials)
        if data["email"] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="Las credenciales son invalidas")