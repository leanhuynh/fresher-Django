from adminlte3.models import Hotel, User
from interface.role_repository_interface import RoleRepositoryInterface
from django.core.exceptions import ObjectDoesNotExist
from django.db import DatabaseError
from django.core.paginator import Paginator
from DjangoWebIDS.common import constant

class HotelRepository(RoleRepositoryInterface):
    
    def __init__(self):
        pass

    # def get_hotel_by_owner_id(self, filters, owner_id):
    #     try :
    #         # Kiểm tra owner có tồn tại không
    #         owner = User.objects.prefetch_related("role").filter(id=owner_id).first()
    #         if not owner:
    #             raise ObjectDoesNotExist("Owner not found")

    #         # Bắt đầu truy vấn Hotel với quan hệ city và user
    #         query = Hotel.objects.select_related("city", "owner")

    #         # Nếu owner không phải admin, chỉ lấy hotel của owner đó
    #         if owner.role.name != constant.ADMIN_ROLE_NAME:
    #             query = query.filter(owner_id=owner_id)

    #         # Lọc theo city_id, hotel_code, name_en
    #         if "city_id" in filters and filters["city_id"]:
    #             query = query.filter(city_id=filters["city_id"])
    #         if "hotel_code" in filters and filters["hotel_code"]:
    #             query = query.filter(hotel_code__icontains=filters["hotel_code"])
    #         if "name_en" in filters and filters["name_en"]:
    #             query = query.filter(name_en__icontains=filters["name_en"])

    #         # Sắp xếp theo name_en
    #         query = query.order_by("name_en")

    #         # Phân trang
    #         paginator = Paginator(query, constant.PAGINATE_DEFAULT)
    #         hotels = paginator.get_page(1)  # Lấy trang đầu tiên

    #         return hotels
    #     except ObjectDoesNotExist as e:
    #         raise e
    #     except DatabaseError:
    #         raise DatabaseError("Database query error")
    #     except Exception as e:
    #         raise Exception("Unknown error")
