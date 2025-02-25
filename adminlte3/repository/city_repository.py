from interface.city_repository_interface import CityRepositoryInterface
from adminlte3.models.city import City

class CityRepository(CityRepositoryInterface):
    
    def __init__(self):
        pass

    def get_all(self):
        return City.objects.all()