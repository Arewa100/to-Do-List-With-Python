from unittest import TestCase
from src.services.implementations.task_service_impl import TaskServiceImpl
from src.dtos.Requests.CreateTaskRequest import CreateTaskRequest
class TestTaskServiceImpl(TestCase):
    def setUp(self):
        self.task_service = TaskServiceImpl()
    def test_that_task_repository_is_empty(self):
        self.assertEqual(self.task_service.task_repository.count(), 0)

    def test_to_add_a_task_task_repository_count_is_one(self):
        create_task_request: CreateTaskRequest = CreateTaskRequest()
        create_task_request.title = "Eat Rice"
        create_task_request.description = "i want to eat rice this evening"
        create_task_request.task_status = False
        create_task_request.user_id = "Miracle"
        self.task_service.add_task(create_task_request)
        self.assertEqual(self.task_service.task_repository.count(), 1)



        ##I AM HERE TESTING
