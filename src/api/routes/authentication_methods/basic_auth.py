from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session

from src.database.connection import get_db
from src.repositories.user_repository import UserRepository
from src.services.password_crypt.check_password import check_password
from src.services.user_service import UserService

router = APIRouter()

security = HTTPBasic()


def authenticate_user(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    user_service = UserService(UserRepository(db))
    user = user_service.get_user_by_email(credentials.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid login")
    is_valid_password = check_password(password=credentials.password, hashed_password=user.password)
    if credentials.username != user.email or not is_valid_password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return user


@router.get("/basic-auth")
def basic_auth(user=Depends(authenticate_user)):
    return {"message": "Authenticated", "username": user.email}
