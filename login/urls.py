from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name = 'login'),
    path('login', views.user_login, name = 'login'),
    path('logout', views.user_logout, name='logout'),
    path("password_reset", views.password_reset_request, name="password_reset")
]