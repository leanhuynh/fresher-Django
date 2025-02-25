from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email field is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Mã hóa mật khẩu
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)  # Tự động tạo id
    first_name = models.CharField(max_length=255)  # Giới hạn 255 ký tự
    last_name = models.CharField(max_length=255)  # Giới hạn 255 ký tự
    user_name = models.CharField(max_length=50, unique=True)  # Giới hạn 50 ký tự, unique    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="users")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)  # Trường ảnh
    email = models.EmailField(unique=True)  # Email, không trùng lặp
    password = models.CharField(max_length=128)  # Mật khẩu (thường được hash)
    last_login_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Ngày tạo
    updated_at = models.DateTimeField(auto_now=True)  # Ngày cập nhật cuối

    objects = UserManager()

    USERNAME_FIELD = 'email'  # Đăng nhập bằng email
    REQUIRED_FIELDS = []  # Không có trường bắt buộc ngoài email

    def soft_delete(self):
        """ Đánh dấu user là đã bị xóa thay vì xóa vĩnh viễn """
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        """ Khôi phục user đã bị soft delete """
        self.deleted_at = None
        self.save()

    def is_deleted(self):
        """ Kiểm tra user có bị soft delete không """
        return self.deleted_at is not None

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-created_at']  # Sắp xếp theo ngày tạo mới nhất