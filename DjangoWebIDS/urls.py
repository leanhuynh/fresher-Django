"""
URL configuration for DjangoWebIDS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  
from django.urls import path  
from adminlte3 import views  
from django.conf import settings
from django.conf.urls.static import static
from adminlte3.controllers.hotel_controller import HotelController
from adminlte3.controllers.role_controller import RoleController
from adminlte3.controllers.user_controller import UserController

urlpatterns = [  
    # path('admin/', admin.site.urls),
    # path('users/', views.index, name='home'),
    # path('users/create', views.create),
    # path('users/edit/<int:id>', views.edit),
    # path('users/search', views.search),
    # path('users/delete', views.delete),
    # path('accounts/login/', views.user_login, name='login'),
    # path('accounts/register/', views.user_register, name='register')

    # GET VIEW URL

    path('hotels/', HotelController.index, name='hotels.index'),
    path('hotels/create', HotelController.create_view, name='hotels.create_view'),
    # path('hotels/edit/<int:id>', HotelController.edit_view, name='hotels.edit_view'),

    path('users/', UserController.index, name='users.index'),
    path('users/profile/<int:id>', UserController.profile, name='users.profile'),
    path('users/create', UserController.create_view, name='users.create_view'),
    # path('users/edit/<int:id>', UserController.edit_view, name='users.edit_view'),

    path('roles/', RoleController.index, name='roles.index'),
    path('roles/create', RoleController.create_view, name='roles.create_view'),
    # path('roles/edit', RoleController.edit_view, name='roles.edit_view'),

    # HANDLE URL

    # path('hotels/create/submit', HotelController.create, name='hotels.create'),
    # path('hotels/edit/<int:id>', HotelController.edit, name='hotels.edit'),

    # path('users/create/submit', UserController.create, name='users.create'),
    # path('users/edit/<int:id>', UserController.edit, name='users.edit'),

    path('roles/create/submit', RoleController.create, name='roles.create'),
    # path('roles/edit/<int:id>', RoleController.edit, name='roles.edit')
]

# Chỉ phục vụ media khi DEBUG = True (môi trường phát triển)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)