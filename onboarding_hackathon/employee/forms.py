from django.forms import ModelForm
from .models import Employee

class EmployAuthForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['identifier', 'password']