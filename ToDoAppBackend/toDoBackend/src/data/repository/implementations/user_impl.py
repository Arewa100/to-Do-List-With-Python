from bson import ObjectId

from src.data.models.user import User
from src.data.repository.interfaces.user_repository_interface import UserRepositoryInterface
from pymongo import MongoClient

class UserRepositoryImpl(UserRepositoryInterface):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.user_repository = client["todolist"]
        self.users_collection = self.user_repository["user"]

    def save(self, user: User):
        user.id = user.username
        self.user_repository.user.insert_one(user.model_dump())
        print(user.id)


    def find_by_id(self, user_id):
        return self.user_repository.user.find_one({"id": user_id})

    def delete_by_id(self, user_id):
        self.user_repository.user.delete_one({"_id": ObjectId(user_id)})

    def find_all(self, user_id):
        users = self.user_repository.user.find({"user_id": user_id})
        return users

    def count(self):
        return self.users_collection.count_documents({})

    def delete_all(self):
        self.users_collection.delete_many({})
