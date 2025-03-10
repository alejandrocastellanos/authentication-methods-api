import uuid

from sqlalchemy.orm import Session

from src.entities.user import User
from src.interfaces.repository_interface import UserRepositoryInterface
from src.models.user import UserModel
from src.services.password_crypt.hash_password import hash_password


class UserRepository(UserRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_email(self, email: str) -> UserModel:
        return self.db.query(UserModel).filter(UserModel.email == email).first()

    def get_user(self, user_id: str) -> UserModel:
        return self.db.query(UserModel).filter(UserModel.id == user_id).first()

    def create_user(self, user: User) -> UserModel:
        user_model = UserModel(
            id=str(uuid.uuid4()),
            email=user.email,
            password=hash_password(user.password)
        )
        self.db.add(user_model)
        self.db.commit()
        self.db.refresh(user_model)
        return user_model
