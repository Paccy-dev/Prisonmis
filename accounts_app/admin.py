from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import *


class UserAdmin(UserAdmin):
    # add_form = RegisterForm
    # form = UserUpdateForm
    model = User
    list_display = ['username', 'email', 'first_name']


admin.site.register(Category),
admin.site.register(Role),
admin.site.register(Employee),
admin.site.register(User, UserAdmin)
