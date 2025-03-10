from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database.connection import get_db
from src.entities.user import User
from src.repositories.user_repository import UserRepository
from src.services.user_service import UserService

router = APIRouter()

@router.post("/users/")
def create_user(user: User, db: Session = Depends(get_db)):
    try:
        user_service = UserService(UserRepository(db))
        user = user_service.create_user(user)
        return {"message": "User created successfully.", "id": user.id}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Error creating user")


@router.get("/users/{user_id}")
def get_user(user_id: str, db: Session = Depends(get_db)):
    service = UserService(UserRepository(db))
    user = service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user.id, "email": user.email}
