from django.db import models
from django.utils import timezone

class RoleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)  # Chỉ lấy các bản ghi chưa bị xóa mềm

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    
    deleted_at = models.DateTimeField(blank=True, null=True)  # Soft delete
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = RoleManager()  # Dùng custom manager để tự động filter các bản ghi chưa bị xóa
    all_objects = models.Manager()  # Cho phép lấy tất cả bản ghi, kể cả bản ghi bị xóa mềm

    def soft_delete(self):
        """ Đánh dấu bản ghi là đã bị xóa mềm """
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        """ Khôi phục bản ghi đã bị xóa mềm """
        self.deleted_at = None
        self.save()

    def __str__(self):
        return self.name
