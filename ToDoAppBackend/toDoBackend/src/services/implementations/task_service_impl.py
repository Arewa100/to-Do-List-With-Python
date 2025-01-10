from src.data.models.task import Task
from src.dtos.Requests.CreateTaskRequest import CreateTaskRequest
from src.dtos.Responses.CreateTaskResponse import CreateTaskResponse
from src.services.interfaces.task_services import TaskService
from src.data.repository.implementations.task_impl import TaskImpl
from src.utils.mapper import create_response_mapper
from src.data.repository.implementations.user_impl import UserRepositoryImpl

class TaskServiceImpl(TaskService):
    def __init__(self):
        self.task_repository = TaskImpl()
        self.user_repository = UserRepositoryImpl()

    def add_task(self, create_task_request: CreateTaskRequest) -> CreateTaskResponse:
        self.__check_if_user_exists__(create_task_request.user_id)
        self.__check_if_task_exists__(create_task_request)
        new_task: Task = Task()
        new_task.title = create_task_request.title
        new_task.description = create_task_request.description
        new_task.task_status = create_task_request.task_status
        new_task.user_id = create_task_request.user_id
        self.task_repository.save(new_task)
        return create_response_mapper(new_task)

    def find_task_by_id(self, task_id, user_id):
        self.__check_if_user_exists__(user_id)
        tasks = self.task_repository.find_all(user_id)   #i am here validating if task_id exists
        for task in tasks:
            if task["task_id"] is not None and  task["task_id"] == task_id:
                return task

    def find_task_by_title(self, title, user_id):
        self.__check_if_user_exists__(user_id)
        self.__check_if_title_exists__(title, user_id)
        tasks = self.task_repository.find_all(user_id)
        for task in tasks:
            if task["title"] == title:
                return task

    def delete_task_by_id(self, task_id, user_id):
        self.__check_if_user_exists__(user_id)
        tasks = self.task_repository.find_all(user_id)
        for task in tasks:
            if task["task_id"] is not None and task["task_id"]== task_id:
                self.task_repository.delete_by_id(task_id)
        return "task deleted successfully"

    def delete_task_by_title(self, title, user_id):
        self.__check_if_user_exists__(user_id)
        self.__check_if_title_exists__(title, user_id)
        tasks = self.task_repository.find_all(user_id)
        for task in tasks:
            if task["title"] == title:
                self.task_repository.delete_by_title(title)
        return "task deleted successfully"

    def update_task(self, task_id):
        pass

    def task_count(self):
        return self.task_repository.count()

    def __check_if_user_exists__(self, user_id):
        found_user = self.user_repository.find_by_id(user_id)
        if found_user is None:
            raise ValueError(f'User {user_id} does not exist')

    def __check_if_task_exists__(self, create_task_request: CreateTaskRequest):
        tasks = self.task_repository.find_all(create_task_request.user_id)
        for task in tasks:
            if task["title"] is not None and task["title"] == create_task_request.title:
                raise ValueError(f'Task {create_task_request.title} already exists')

    def __check_if_title_exists__(self, title, user_id):
        tasks = self.task_repository.find_all(user_id)
        for task in tasks:
            if task["title"] is None or task["title"] != title:
                raise ValueError(f'Title {title} does not exists')

