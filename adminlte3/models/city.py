from django.db import models
from django.utils import timezone

class City(models.Model):
    id = models.AutoField(primary_key=True)  # Tự động tạo id
    name = models.CharField(max_length=255, unique=True)  # Tên thành phố, duy nhất
    description = models.TextField(blank=True, null=True)  # Mô tả, có thể để trống

    deleted_at = models.DateTimeField(blank=True, null=True)  # Soft delete
    created_at = models.DateTimeField(auto_now_add=True)  # Ngày tạo
    updated_at = models.DateTimeField(auto_now=True)  # Ngày cập nhật cuối

    def soft_delete(self):
        """ Đánh dấu city là đã bị xóa thay vì xóa vĩnh viễn """
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        """ Khôi phục city đã bị soft delete """
        self.deleted_at = None
        self.save()

    def is_deleted(self):
        """ Kiểm tra city có bị xóa mềm không """
        return self.deleted_at is not None

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']  # Sắp xếp theo tên
