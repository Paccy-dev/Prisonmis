from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',posts_view,name='posts'),
    path('add/',post_add_view,name='post_add'),
    path('<int:pk>/',post_details_view,name='post_details'),
    path('<int:pk>/update',post_update_view,name='post_update'),
    path('<int:pk>/delete',post_delete_view,name='post_delete'),
]