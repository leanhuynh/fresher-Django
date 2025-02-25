from abc import ABC, abstractmethod

class RoleRepositoryInterface(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def find_role_by_id(self, id):
        pass

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def update(self, data, id):
        pass

    @abstractmethod
    def search(self, filters):
        pass

    @abstractmethod
    def deleteRole(self, role_id, auth_id):
        pass