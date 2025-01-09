from bson import ObjectId

from src.data.models.task import Task
from src.data.repository.interfaces.task_repository import TaskRepository
from pymongo import MongoClient



class TaskImpl(TaskRepository):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.task_repository = client["todolist"]
        self.collection_of_task = self.task_repository["task"]

    def save(self, task: Task):
        self.task_repository.task.insert_one(task.model_dump())
        task.task_id = self.collection_of_task.find_one({"task_id": task.task_id})["_id"]
        the_task = ({"_id": ObjectId(task.task_id)})
        self.collection_of_task.update_one(the_task, {"$set": task.model_dump()})

    def find_by_id(self, task_id):
        return self.task_repository.task.find_one({"_id": ObjectId(task_id)})

    def delete_by_id(self, task_id):
        self.task_repository.task.delete_one({"_id": ObjectId(task_id)})

    def find_all(self, user_id):
        tasks =  self.task_repository.task.find({"user_id": user_id})
        return tasks

    def count(self):
        return self.collection_of_task.count_documents({})

    def delete_all(self):
        self.collection_of_task.drop()
