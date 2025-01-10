from abc import ABC, abstractmethod
from src.dtos.Requests.CreateTaskRequest import CreateTaskRequest
from src.dtos.Responses.CreateTaskResponse import CreateTaskResponse


class TaskService(ABC):

    @abstractmethod
    def add_task(self, create_task_request: CreateTaskRequest) -> CreateTaskResponse:
        pass

    @abstractmethod
    def find_task_by_id(self, task_id, user_id):
        pass

    @abstractmethod
    def find_task_by_title(self, title, user_id):
        pass

    @abstractmethod
    def delete_task_by_id(self, task_id, user_id):
        pass

    @abstractmethod
    def delete_task_by_title(self, title, user_id):
        pass

    @abstractmethod
    def update_task(self, task_id):
        pass
    @abstractmethod
    def task_count(self):
        pass

