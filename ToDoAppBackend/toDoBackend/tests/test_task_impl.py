from unittest import TestCase
from src.data.repository.implementations.task_impl import TaskImpl
from src.data.models.task import Task

class TestTaskImpl(TestCase):
    def setUp(self):
        self.task_repository = TaskImpl()

    def test_that_mongo_repository_is_empty(self):
        self.task_repository.delete_all()
        self.assertEqual(self.task_repository.count(), 0)

    def test_to_add_one_task_count_is_two(self):
        self.task_repository.delete_all()
        task:Task = Task(title="Wedding", description="it is coming", task_status=False, task_id="faith", user_id="Miracle")
        self.task_repository.save(task)
        self.assertEqual(self.task_repository.count(), 1)

    def test_to_save_one_task_and_find_task_by_id(self):
        self.task_repository.delete_all()
        task: Task = Task(title="swimming", description="it is coming", task_status=False ,user_id="Miracle")
        self.task_repository.save(task)
        self.assertEqual(self.task_repository.find_by_id(task.task_id)["title"], task.title)

    def test_to_delete_task_by_id_count_is_zero(self):
        self.task_repository.delete_all()
        task: Task = Task(title="play", description="it is coming", task_status=False, user_id="Miracle")
        self.task_repository.save(task)
        self.assertEqual(self.task_repository.count(), 1)
        self.task_repository.delete_by_id(task.task_id)
        self.assertEqual(self.task_repository.count(), 0)

    def test_to_save_tasks_and_get_all_tasks_by_user_name(self):
        task: Task = Task(title="play", description="it is coming", task_status=False, user_id="Ope")
        self.task_repository.save(task)
        task_two: Task = Task(title="secondPlay", description="it is coming", task_status=False, user_id="Miracle")
        self.task_repository.save(task_two)
        print(str(self.task_repository.find_all(user_id="Miracle")))




