from src.data.models.task import Task
from src.dtos.Requests.CreateTaskRequest import CreateTaskRequest
from src.dtos.Responses.CreateTaskResponse import CreateTaskResponse
from src.services.interfaces.task_services import TaskService
from src.data.repository.implementations.task_impl import TaskImpl
from src.utils.mapper import create_response_mapper

class TaskServiceImpl(TaskService):
    def __init__(self):
        self.task_repository = TaskImpl()
    def add_task(self, create_task_request: CreateTaskRequest) -> CreateTaskResponse:
        new_task: Task = Task()
        new_task.title = create_task_request.title
        new_task.description = create_task_request.description
        new_task.task_status = create_task_request.task_status
        new_task.user_id = create_task_request.user_id
        self.task_repository.save(new_task)
        return create_response_mapper(new_task)

    def find_task(self, task_id):
        pass

    def delete_task(self, task_id):
        pass

    def update_task(self, task_id):
        pass

    def task_count(self):
        return self.task_repository.count()

