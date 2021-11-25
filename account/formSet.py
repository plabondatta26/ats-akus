from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = ['username', 'first_name', 'last_name', 'contact', 'address', 'password1', 'password2', ]
