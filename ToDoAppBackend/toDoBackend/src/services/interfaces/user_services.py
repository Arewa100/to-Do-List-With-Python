from abc import ABC, abstractmethod

class UserService(ABC):
    @abstractmethod
    def add_user(self, user):
        pass

    @abstractmethod
    def find_user(self, user_id):
        pass

    @abstractmethod
    def add_task(self, task):
        pass

    @abstractmethod
    def find_task(self, task_id):
        pass

    @abstractmethod
    def delete_task(self, task_id):
        pass

    @abstractmethod
    def update_task(self, task_id):
        pass