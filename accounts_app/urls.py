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
    path('users/',users_view,name='users'),
    path('users/add/',user_add_view,name='user_add'),
    path('users/<int:pk>/',user_details_view,name='user_details'),
    path('users/<int:pk>/update/',user_update_view,name='user_update'),
    path('users/<int:pk>/delete/',user_delete_view,name='user_delete'),
    
]
