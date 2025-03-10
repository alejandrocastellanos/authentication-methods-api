import jwt

from fastapi import HTTPException

from src.entities.user import User
from src.utils.settings import SECRET_KEY, ALGORITHM


def verify_jwt(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return User(email=payload.get("sub"))
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
