from abc import ABC, abstractmethod

class HotelRepositoryInterface(ABC):
    @abstractmethod
    def get_hotels_by_owner_id(self, filters, owner_id):
        pass
    
    @abstractmethod
    def find_hotel_by_id(self, hotel_id):
        pass

    @abstractmethod
    def create_hotel(self, data, owner_id):
        pass

    @abstractmethod
    def search_hotels(self, filters):
        pass

    @abstractmethod
    def update_hotel(self, data, hotel_id):
        pass

    @abstractmethod
    def delete_hotel(self, hotel_id, owner_id):
        pass