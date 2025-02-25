from django.db import models
from django.utils import timezone
from .user import User
from .city import City

class Hotel(models.Model):
    id = models.AutoField(primary_key=True)  # Tự động tạo id
    owner = models.ForeignKey(User, on_delete=models.RESTRICT)  # Liên kết với User
    city = models.ForeignKey(City, on_delete=models.RESTRICT)  # Liên kết với City
    name_en = models.CharField(max_length=255, unique=True)  # Tên tiếng Anh
    name_jp = models.CharField(max_length=255, unique=True)  # Tên tiếng Nhật
    telephone = models.CharField(max_length=255)  # Số điện thoại
    fax = models.CharField(max_length=255, blank=True, null=True)  # Fax (có thể trống)
    company_name = models.CharField(max_length=255)  # Tên công ty
    tax_code = models.CharField(max_length=13, blank=True, null=True)  # Mã số thuế
    hotel_code = models.CharField(max_length=6, unique=True)  # Mã khách sạn (6 ký tự)
    email = models.EmailField(max_length=255)  # Email khách sạn
    address_1 = models.CharField(max_length=255)  # Địa chỉ 1
    address_2 = models.CharField(max_length=255, blank=True, null=True)  # Địa chỉ 2 (có thể trống)

    deleted_at = models.DateTimeField(blank=True, null=True)  # Soft delete
    created_at = models.DateTimeField(auto_now_add=True)  # Ngày tạo
    updated_at = models.DateTimeField(auto_now=True)  # Ngày cập nhật

    def soft_delete(self):
        """ Đánh dấu khách sạn đã bị xóa thay vì xóa vĩnh viễn """
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        """ Khôi phục khách sạn đã bị soft delete """
        self.deleted_at = None
        self.save()

    def is_deleted(self):
        """ Kiểm tra khách sạn có bị xóa mềm không """
        return self.deleted_at is not None

    def __str__(self):
        return f"{self.name_en} - {self.city.name}"

    class Meta:
        ordering = ['-created_at']