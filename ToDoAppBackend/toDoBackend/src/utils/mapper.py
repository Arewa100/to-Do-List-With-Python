from src.data.models.task import Task
from src.dtos.Responses.CreateTaskResponse import CreateTaskResponse


def create_response_mapper(created_task: Task) -> CreateTaskResponse:
    create_new_response = CreateTaskResponse()
    create_new_response.title = str(created_task.title)
    create_new_response.description = str(created_task.description)
    create_new_response.task_status = str(created_task.task_status)
    create_new_response.user_id = str(created_task.user_id)
    create_new_response.task_id = str(created_task.task_id)
    create_new_response.date_created = str(created_task.date_created)
    return create_new_response