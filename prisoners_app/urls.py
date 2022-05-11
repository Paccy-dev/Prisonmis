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
    path('cases/',cases_view,name='cases'),
    path('cases/add',case_add_view,name='case_add'),
    path('cases/<int:pk>/',case_details_view,name='case_details'),
    path('cases/<int:pk>/update/',case_update_view,name='case_update'),
    path('cases/<int:pk>/delete/',case_delete_view,name='case_delete'),
    path('leaves/',leaves_view,name='leaves'),
    path('leaves/add/',leave_add_view,name='leave_add'),
    path('leaves/<int:pk>/',leave_details_view,name='leave_details'),
    path('leaves/<int:pk>/update/',leave_update_view,name='leave_update'),
    path('leaves/<int:pk>/delete/',leave_delete_view,name='leave_delete'),
    path('',prisoners_view,name='prisoners'),
    path('add/',prisoner_add_view,name='prisoner_add'),
    path('<int:pk>/',prisoner_details_view,name='prisoner_details'),
    path('<int:pk>/update/',prisoner_update_view,name='prisoner_update'),
    path('<int:pk>/delete/',prisoner_delete_view,name='prisoner_delete'),
    path('visits/',visits_view,name='visits'),
    path('visits/add/',visit_add_view,name='visit_add'),
    path('visits/<int:pk>/',visit_details_view,name='visit_details'),
    path('visits/<int:pk>/update/',visit_update_view,name='visit_update'),
    path('visits/<int:pk>/delete/',visit_delete_view,name='visit_delete'),
    path('visitors/',visitors_view,name='visitors'),
    path('visitors/add/',visitor_add_view,name='visitor_add'),
    path('visitors/<int:pk>/',visitor_details_view,name='visitor_details'),
    path('visitors/<int:pk>/update/',visitor_update_view,name='visitor_update'),
    path('visitors/<int:pk>/delete/',visitor_delete_view,name='visitor_delete'),
]
