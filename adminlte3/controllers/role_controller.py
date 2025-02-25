from adminlte3.services.hotel_service import HotelService
from adminlte3.services.user_service import UserService
from adminlte3.services.role_service import RoleService
from adminlte3.services.city_service import CityService
from adminlte3.form.role_form import RoleForm
from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse
from DjangoWebIDS.common.status_code import StatusCode
from django.shortcuts import redirect
from adminlte3.models.role import Role


class RoleController:

    def __init__(self):
        self._role_service = RoleService

    @staticmethod
    def index(request):
        try:
            return render(request, '../templates/adminlte/role/index.html')
        except Exception as e:
            return JsonResponse({'message': f'Error: {str(e)}'}, status=400)
        
    @staticmethod
    def create_view(request):
        try:
            return render(request, '../templates/adminlte/role/create.html')
        except Exception as e:
            return JsonResponse({'message': f'Error: {str(e)}'}, status=400)
    
    @staticmethod
    def edit_view(request):
        try:
            return render(request, '../templates/adminlte/role/edit.html')
        except Exception as e:
            return JsonResponse({'message': f'Error: {str(e)}'}, status=400)
        
    @staticmethod
    def create(request):
        try:
            if request.method == "POST":
                form = RoleForm(request.POST, request.FILES)
                if form.is_valid() == False:
                    raise Exception({'message': 'Form is invalid', 'status': StatusCode.HTTP_STATUS_BAD_REQUEST})
                
                cleaned_data = form.cleaned_data
                new_role = Role(
                    # name_en = cleaned_data['name_en'],
                    # name_jp = cleaned_data['name_jp'],
                    # city_id = cleaned_data['city'],
                    # owner_id = request.user.id,
                    # hotel_code = cleaned_data['hotel_code'],
                    # company_name = cleaned_data['company_name'],
                    # email = cleaned_data['email'],
                    # telephone = cleaned_data['telephone'],
                    # fax = cleaned_data['fax'],
                    # tax_code = cleaned_data['tax_code'],
                    # address_1 = cleaned_data['address_1'],
                    # address_2 = cleaned_data['address_2']
                    name = cleaned_data['name'],
                    description = cleaned_data['description']
                )
                new_role.save()

                messages.success(request, 'Create role successfully!')
                return redirect(request.META.get('HTTP_REFERER', 'home'))  # Quay lại trang trước, nếu không có thì về trang chủ
            else:
                raise Exception({'message': 'Method is not allowed', 'status': StatusCode.HTTP_STATUS_NOT_ACCEPTABLE})
        except Exception as e:
            return JsonResponse({'message': str(e.args[0]['message']) + '!'}, status=int(e.args[0]['status']))

