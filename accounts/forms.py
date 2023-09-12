from django import forms
from django.contrib.auth.forms import UserCreateionForm
from django.contrib.auth.models import User
from accounts.models import myuser

class UserForm(UserCreateionForm):
    class Meta:
        model = myuser
        fields = ("username")