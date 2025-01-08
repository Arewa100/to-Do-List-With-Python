from bson import ObjectId

from src.data.models.task import Task
from src.data.repository.interfaces.task_repository import TaskRepository
from pymongo import MongoClient



class TaskImpl(TaskRepository):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.task_repository = client["task"]
        self.collection_of_task = self.task_repository["task"]

    def save(self, task: Task):
        self.task_repository.task.insert_one(task)

    def find_by_id(self, task_id):
        self.task_repository.task.find_one({"_id": ObjectId(task_id)})

    def delete_by_id(self, task_id):
        self.task_repository.task.delete_one({"_id": ObjectId(task_id)})

    def find_all(self):
        tasks = list( self.task_repository.task.find())
        return tasks