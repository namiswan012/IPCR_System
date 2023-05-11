from django.urls import path
from . import views

urlpatterns = [
    path('member_home', views.member_home, name='member_home'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('superadmin_home', views.superadmin_home, name='superadmin_home'),
]
