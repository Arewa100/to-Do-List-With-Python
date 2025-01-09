from abc import abstractmethod, ABC
from src.data.models.user import User


class UserRepositoryInterface(ABC):
    @abstractmethod
    def save(self, user: User):
        pass
    @abstractmethod
    def find_by_id(self, user_id):
        pass
    @abstractmethod
    def delete_by_id(self, user_id):
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


