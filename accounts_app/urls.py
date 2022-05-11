"""prisonmis URL Configuration

The `urlpatterns` list routes URLs to  For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('categorys/',categorys_view,name='categorys'),
    path('categorys/add/',category_add_view,name='category_add'),
    path('categorys/<int:pk>/',category_details_view,name='category_details'),
    path('categorys/<int:pk>/update/',category_update_view,name='category_update'),
    path('categorys/<int:pk>/delete/',category_delete_view,name='category_delete'),
    path('roles/',roles_view,name='roles'),
    path('roles/add/',role_add_view,name='role_add'),
    path('roles/<int:pk>/',role_details_view,name='role_details'),
    path('roles/<int:pk>/update/',role_update_view,name='role_update'),
    path('roles/<int:pk>/delete/',role_delete_view,name='role_delete'),
    path('employees/',employees_view,name='employees'),
    path('employees/add/',employee_add_view,name='employee_add'),
    path('employees/<int:pk>/',employee_details_view,name='employee_details'),
    path('employees/<int:pk>/update/',employee_update_view,name='employee_update'),
    path('employees/<int:pk>/delete/',employee_delete_view,name='employee_delete'),
    path('users/',users_view,name='users'),
    path('users/add/',user_add_view,name='user_add'),
    path('users/<int:pk>/',user_details_view,name='user_details'),
    path('users/<int:pk>/update/',user_update_view,name='users_update'),
    path('users/<int:pk>/delete/',user_delete_view,name='users_delete'),
    
]
