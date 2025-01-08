from src.data.models.user import User
from src.data.repository.interfaces.user_repository_interface import UserRepositoryInterface
from pymongo import MongoClient

class UserRepositoryImpl(UserRepositoryInterface):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.user_repository = client["users"]
    def save(self, user: User):
        self.user_repository.user.insert_one(user.__dict__)  #i am here
        pass

    def find_by_id(self, user_id):
        pass

    def delete_by_id(self, user_id):
        pass

    def find_all(self):
        pass