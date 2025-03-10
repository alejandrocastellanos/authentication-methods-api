from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.database.connection import get_db
from src.entities.token import Token
from src.repositories.user_repository import UserRepository
from src.services.jwt.create_jwt import create_jwt
from src.services.jwt.verify_jwt import verify_jwt
from src.services.password_crypt.check_password import check_password
from src.services.user_service import UserService

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/jwt-auth", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user_service = UserService(UserRepository(db))
    user = user_service.get_user_by_email(form_data.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid login")
    is_valid_password = check_password(password=form_data.password, hashed_password=user.password)
    if not is_valid_password:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_jwt({"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/jwt-auth-bearer")
def jwt_auth(token: str = Depends(oauth2_scheme)):
    return {"message": "Authenticated", "user": verify_jwt(token).email}
