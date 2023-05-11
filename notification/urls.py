from django.urls import path
from . import views

urlpatterns = [
    path('member_notification', views.member_notification, name='member_notification'),

]