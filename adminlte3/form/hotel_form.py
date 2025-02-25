from django import forms
from django.core.exceptions import ValidationError
from adminlte3.models.hotel import Hotel
from adminlte3.models.city import City
import re

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = [
            'name_en', 'name_jp', 'city_id', 'hotel_code',
            'company_name', 'email', 'telephone', 'fax',
            'tax_code', 'address_1', 'address_2'
        ]
        error_messages = {
            'name_en': {
                'required': 'This field is required.',
                'max_length': 'Cannot exceed 255 characters.',
                'unique': 'This name already exists.',
                'regex': 'Only letters, numbers, and spaces are allowed.'
            },
            'name_jp': {
                'required': 'This field is required.',
                'max_length': 'Cannot exceed 255 characters.',
                'unique': 'This name already exists.',
                'regex': 'Only letters, numbers, and spaces are allowed.'
            },
            'hotel_code': {
                'required': 'This field is required.',
                'min_length': 'Hotel code must be exactly 6 characters.',
                'max_length': 'Hotel code must be exactly 6 characters.',
                'regex': 'Only alphanumeric characters are allowed.',
                'unique': 'This hotel code already exists.'
            },
            'telephone': {
                'regex': 'Invalid phone format. Only numbers, dashes, and spaces are allowed.'
            },
            'fax': {
                'regex': 'Invalid fax format. Only numbers, dashes, and spaces are allowed.'
            },
            'tax_code': {
                'min_length': 'Tax code must be at least 10 characters.',
                'max_length': 'Tax code cannot exceed 13 characters.',
                'regex': 'Tax code must contain only numbers.'
            }
        }

    def clean_name_en(self):
        name_en = self.cleaned_data.get('name_en')
        if not name_en:
            raise ValidationError('This field is required.')
        if len(name_en) > 255:
            raise ValidationError('Cannot exceed 255 characters.')
        if not re.match(r'^[\w\s]+$', name_en):  # Regex cho chữ cái, số và khoảng trắng
            raise ValidationError('Only letters, numbers, and spaces are allowed.')
        if Hotel.objects.filter(name_en=name_en).exists():
            raise ValidationError('This name already exists.')
        return name_en

    def clean_name_jp(self):
        name_jp = self.cleaned_data.get('name_jp')
        if not name_jp:
            raise ValidationError('This field is required.')
        if len(name_jp) > 255:
            raise ValidationError('Cannot exceed 255 characters.')
        if not re.match(r'^[\w\s]+$', name_jp):  
            raise ValidationError('Only letters, numbers, and spaces are allowed.')
        if Hotel.objects.filter(name_jp=name_jp).exists():
            raise ValidationError('This name already exists.')
        return name_jp

    def clean_hotel_code(self):
        hotel_code = self.cleaned_data.get('hotel_code')
        if not hotel_code:
            raise ValidationError('This field is required.')
        if len(hotel_code) != 6:
            raise ValidationError('Hotel code must be exactly 6 characters.')
        if not hotel_code.isalnum():
            raise ValidationError('Only alphanumeric characters are allowed.')
        if Hotel.objects.filter(hotel_code=hotel_code).exists():
            raise ValidationError('This hotel code already exists.')
        return hotel_code

    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        if not re.match(r'^\+?[0-9\-\s]+$', telephone):
            raise ValidationError('Invalid phone format. Only numbers, dashes, and spaces are allowed.')
        return telephone

    def clean_fax(self):
        fax = self.cleaned_data.get('fax')
        if fax and not re.match(r'^\+?[0-9\-\s]+$', fax):
            raise ValidationError('Invalid fax format. Only numbers, dashes, and spaces are allowed.')
        return fax

    def clean_tax_code(self):
        tax_code = self.cleaned_data.get('tax_code')
        if tax_code and (len(tax_code) < 10 or len(tax_code) > 13):
            raise ValidationError('Tax code must be between 10 and 13 characters.')
        if tax_code and not tax_code.isdigit():
            raise ValidationError('Tax code must contain only numbers.')
        return tax_code
