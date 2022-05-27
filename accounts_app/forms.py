from re import A
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from .models import *

class Category_Form(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class User_Form(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username','email','category','password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(User_Form, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = "Password must contain at least 8 characters."
        self.fields['password2'].label = "Password confirm"
        self.fields['username'].help_text = " Letters and digits."      
        self.fields['username'].label = "User ID"  

class Login_Form(AuthenticationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username','email','category','photo'] 
    def __init__(self, *args, **kwargs):
        super(Login_Form, self).__init__(*args, **kwargs)     
        self.fields['username'].label = "User ID"  
       

class Profile_Form(UserChangeForm):
    # email = forms.EmailField(required=False)
    # image = forms.ImageField(required=False)
    # phone = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username','email','category','photo']

    def __init__(self, *args, **kwargs):
        super(Profile_Form, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = " Letters and digits."
        self.fields['username'].label = "User ID"
