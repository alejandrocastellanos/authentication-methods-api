from src.entities.user import User
from src.interfaces.repository_interface import UserRepositoryInterface


class UserService:

    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def create_user(self, user: User):
        return self.user_repository.create_user(user)

    def get_user(self, user_id: str):
        return self.user_repository.get_user(user_id)

    def get_user_by_email(self, email: str):
        return self.user_repository.get_user_by_email(email)
