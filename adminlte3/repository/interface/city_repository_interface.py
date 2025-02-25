from abc import ABC, abstractmethod

class CityRepositoryInterface(ABC):
    @abstractmethod
    def get_all(self):
        pass