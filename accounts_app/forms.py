from re import A
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *

class Category_Form(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class Role_Form(forms.ModelForm):
    class Meta:
        model = Role
        fields = "__all__"

class Employee_Form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class User_Form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

Login_Form = AuthenticationForm

