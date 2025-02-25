from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from adminlte3.models.role import Role

import re

class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        min_length=8,
        max_length=16,
        required=True,
        error_messages={
            'required': 'Password is required.',
            'min_length': 'Password must be at least 8 characters long.',
            'max_length': 'Password cannot exceed 16 characters.',
        }
    )
    password_confirmation = forms.CharField(
        widget=forms.PasswordInput(),
        required=True
    )
    avatar = forms.ImageField(
        required=False,
        error_messages={'invalid': 'Invalid image format.'}
    )
    role_id = forms.ModelChoiceField(
        queryset=Role.objects.all(),
        empty_label="--Select Role--",
        required=False,
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'user_name', 'email', 'address', 'password', 'role_id', 'avatar']

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        if not re.match(r'^[a-zA-Z0-9._]+$', user_name):
            raise ValidationError("Username can only contain letters, numbers, dots, and underscores.")
        if User.objects.filter(user_name=user_name).exists():
            raise ValidationError("This username is already taken.")
        return user_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if password != password_confirmation:
            raise ValidationError("Passwords do not match.")
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]+$', password):
            raise ValidationError("Password must contain letters, numbers, and special characters.")
        return password

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if avatar:
            if avatar.size > 2 * 1024 * 1024:
                raise ValidationError("Avatar size must be less than 2MB.")
            if not avatar.content_type in ["image/jpeg", "image/png", "image/jpg", "image/gif", "image/svg+xml"]:
                raise ValidationError("Invalid image format. Allowed formats: jpeg, png, jpg, gif, svg.")
        return avatar
