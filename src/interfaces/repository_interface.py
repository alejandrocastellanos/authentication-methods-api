from abc import ABC, abstractmethod

from src.entities.user import User
from src.models.user import UserModel


class UserRepositoryInterface(ABC):

    @abstractmethod
    def get_user_by_email(self, email: str) -> UserModel:
        pass

    @abstractmethod
    def get_user(self, user_id: str) -> UserModel:
        pass

    @abstractmethod
    def create_user(self, user: User) -> UserModel:
        pass
