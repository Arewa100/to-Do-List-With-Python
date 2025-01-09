from abc import ABC, abstractmethod

from src.data.models.task import Task

class TaskRepository(ABC):
    @abstractmethod
    def save(self, task:Task):
        pass

    @abstractmethod
    def find_by_id(self, task_id):
        pass

    @abstractmethod
    def delete_by_id(self, task_id):
        pass

    @abstractmethod
    def find_all(self, user_id):
        pass
    @abstractmethod
    def count(self):
        pass
    @abstractmethod
    def delete_all(self):
        pass