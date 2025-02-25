from django import forms
from django.core.exceptions import ValidationError
from adminlte3.models.role import Role
import re

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name', 'description']
        error_messages = {
            'name': {
                'required': 'This field is required.',
                'max_length': 'Name cannot exceed 255 characters.',
                'unique': 'This name already exists.',
                'string': 'Name must be a valid string.',
                'regex': 'Invalid name format.',
            },
            'description': {
                'max_length': 'Description cannot exceed 255 characters.',
                'string': 'Description must be a valid string.',
            }
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise ValidationError('This field is required.')
        if len(name) > 255:
            raise ValidationError('Name cannot exceed 255 characters.')
        if not re.match(r'^[a-zA-Z0-9\s\-_]+$', name):  # Regex kiểm tra ký tự hợp lệ
            raise ValidationError('Invalid name format.')
        if Role.objects.filter(name=name).exists():
            raise ValidationError('This name already exists.')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description and len(description) > 255:
            raise ValidationError('Description cannot exceed 255 characters.')
        return description