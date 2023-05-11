from django.urls import path
from . import views

urlpatterns = [
    path('member_faculty_list', views.member_faculty_list, name='member_faculty_list'),
]