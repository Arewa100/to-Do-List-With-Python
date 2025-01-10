from unittest import TestCase

from src.data.models.user import User
from src.data.repository.implementations.task_impl import TaskImpl
from src.data.repository.implementations.user_impl import UserRepositoryImpl
from src.dtos.Responses.CreateTaskResponse import CreateTaskResponse
from src.services.implementations.task_service_impl import TaskServiceImpl
from src.dtos.Requests.CreateTaskRequest import CreateTaskRequest
class TestTaskServiceImpl(TestCase):
    def setUp(self):
        self.task_service = TaskServiceImpl()
        self.task_repository = TaskImpl()
        self.user_repository: UserRepositoryImpl = UserRepositoryImpl()

    def __create_a_user__(self, username):
        user: User = User()
        user.username= username
        user.email = "<EMAIL>"
        user.password = "<PASSWORD>"
        self.user_repository.save(user)

    def clear_repos(self):
        self.task_repository.delete_all()
        self.user_repository.delete_all()

    def test_that_task_repository_is_empty(self):
        self.clear_repos()
        self.assertEqual(self.task_service.task_repository.count(), 0)

    def test_to_add_a_task_task_repository_count_is_one(self):
        self.clear_repos()
        create_task_request: CreateTaskRequest = CreateTaskRequest()
        create_task_request.title = "Eat Rice"
        create_task_request.description = "i want to eat rice this evening"
        create_task_request.task_status = False
        self.__create_a_user__("Arewa")
        create_task_request.user_id = "Arewa"
        self.task_service.add_task(create_task_request)
        self.assertEqual(self.task_service.task_repository.count(), 1)

        create_task_request_two: CreateTaskRequest = CreateTaskRequest()
        create_task_request_two.title = "Eat Rice"
        create_task_request_two.description = "i want to eat rice this evening"
        create_task_request_two.task_status = False
        self.__create_a_user__("Ope")
        create_task_request_two.user_id = "Ope"
        self.task_service.add_task(create_task_request_two)
        self.assertEqual(self.task_service.task_repository.count(), 2)

    def test_to_add_a_task_that_with_a_user_that_does_not_exist_exception_is_raised(self):
        self.clear_repos()
        create_task_request: CreateTaskRequest = CreateTaskRequest()
        create_task_request.title = "sleeping"
        create_task_request.description = "try to sleep by 12 pm"
        create_task_request.task_status = False
        create_task_request.user_id = "Miracle"
        self.assertRaises(ValueError, self.task_service.add_task, create_task_request)

    def test_that_to_add_a_task_exception_is_raised_if_task_exists(self):
        self.clear_repos()
        create_task_request: CreateTaskRequest = CreateTaskRequest()
        create_task_request.title = "Eat Rice"
        create_task_request.description = "i want to eat rice this evening"
        create_task_request.task_status = False
        self.__create_a_user__("Arewa")
        create_task_request.user_id = "Arewa"
        self.task_service.add_task(create_task_request)

        create_task_request_two: CreateTaskRequest = CreateTaskRequest()
        create_task_request_two.title = "Eat Rice"
        create_task_request_two.description = "No i want beans"
        create_task_request_two.task_status = False
        self.__create_a_user__("Opeyemi")
        create_task_request_two.user_id = "Opeyemi"
        self.assertRaises(ValueError, self.task_service.add_task, create_task_request_two)

    def test_to_add_a_task_and_find_task_by_id(self):
        self.clear_repos()
        create_task_request: CreateTaskRequest = CreateTaskRequest()
        create_task_request.title = "Football"
        create_task_request.description = "i want to play football this evening"
        create_task_request.task_status = False
        self.__create_a_user__("Arewa")
        create_task_request.user_id = "Arewa"
        create_task_response: CreateTaskResponse = self.task_service.add_task(create_task_request)
        self.assertEqual(self.task_service.find_task_by_id(create_task_response.task_id, "Arewa")["description"], create_task_request.description)

    def test_to_add_task_and_find_task_by_title(self):
        self.clear_repos()
        create_task_request: CreateTaskRequest = CreateTaskRequest()
        create_task_request.title = "Football"
        create_task_request.description = "i want to play football this evening"
        create_task_request.task_status = False
        self.__create_a_user__("Arewa")
        create_task_request.user_id = "Arewa"
        create_task_response: CreateTaskResponse = self.task_service.add_task(create_task_request)
        self.assertEqual(self.task_service.find_task_by_title(create_task_response.title, "Arewa")["description"],create_task_request.description)

    def test_to_add_task_and_delete_the_task_id(self):
        self.clear_repos()
        create_task_request: CreateTaskRequest = CreateTaskRequest()
        create_task_request.title = "washing"
        create_task_request.description = "i am doing my laundry this evening"
        create_task_request.task_status = False
        self.__create_a_user__("Arewa")
        create_task_request.user_id = "Arewa"
        create_task_response: CreateTaskResponse = self.task_service.add_task(create_task_request)
        self.assertEqual(self.task_service.task_count(), 1)
        self.task_service.delete_task_by_id(create_task_response.task_id, "Arewa")
        self.assertEqual(self.task_service.task_count(), 0)

    def test_to_add_task_and_delete_task_by_title(self):
        self.clear_repos()
        create_task_request: CreateTaskRequest = CreateTaskRequest()
        create_task_request.title = "washing"
        create_task_request.description = "i am doing my laundry this evening"
        create_task_request.task_status = False
        self.__create_a_user__("Arewa")
        create_task_request.user_id = "Arewa"
        create_task_response: CreateTaskResponse = self.task_service.add_task(create_task_request)
        self.assertEqual(self.task_service.task_count(), 1)
        self.task_service.delete_task_by_title(create_task_response.title, "Arewa")
        self.assertEqual(self.task_service.task_count(), 0)

