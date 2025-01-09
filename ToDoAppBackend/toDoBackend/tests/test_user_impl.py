from unittest import TestCase

from src.data.models.user import User
from src.data.repository.implementations.user_impl import UserRepositoryImpl


class TestUserRepositoryImpl(TestCase):
    def setUp(self):
        self.user_repository: UserRepositoryImpl = UserRepositoryImpl()

    def test_that_user_repository_is_empty(self):
        self.user_repository.delete_all()
        self.assertEqual(self.user_repository.count(), 0)

    def test_to_add_user_repository_count_is_zero(self):
        self.user_repository.delete_all()
        user: User = User(username="Arewa", email="<EMAIL>", password="<PASSWORD>")
        self.user_repository.save(user)
        self.assertEqual(self.user_repository.count(), 1)
        self.user_repository.delete_all()
        self.assertEqual(self.user_repository.count(), 0)

    def test_to_add_user_and_find_user_by_id(self):
        self.user_repository.delete_all()
        user: User = User(username="Arewa", email="olasoyinmiracle@gamil.com", password="<PASSWORD>")
        self.user_repository.save(user)
        self.assertEqual(self.user_repository.count(), 1)
        self.assertEqual(self.user_repository.find_by_id(user.id)["username"], "Arewa")








