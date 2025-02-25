from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def find_user_by_id(self, id):
        pass

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def update(self, data, id):
        pass

    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def search(self, filters):
        pass

    @abstractmethod
    def get_user_profile_by_id(self, id):
        pass