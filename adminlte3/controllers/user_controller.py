from adminlte3.services.hotel_service import HotelService
from adminlte3.services.user_service import UserService
from adminlte3.services.role_service import RoleService
from adminlte3.services.city_service import CityService
from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse

class UserController():

    def __init__(self):
        self._user_service = UserService

    @staticmethod
    def index(request):
        try:
            return render(request, '../templates/adminlte/user/index.html')
        except Exception as e:
            return JsonResponse({'message': f'Error: {str(e)}'}, status=400) 
    
    @staticmethod
    def profile(request):
        try:
            return render(request, '../templates/adminlte/user/profile.html')
        except Exception as e:
            return JsonResponse({'message': f'Error: {str(e)}'}, status=400)
        
    @staticmethod
    def create_view(request):
        try:
            return render(request, '../templates/adminlte/user/create.html')
        except Exception as e:
            return JsonResponse({'message': f'Error: {str(e)}'}, status=400)
        
    @staticmethod
    def edit_view(request):
        try:
            return render(request, '../templates/adminlte/user/edit.html')
        except Exception as e:
            return JsonResponse({'message': f'Error: {str(e)}'}, status=400)
