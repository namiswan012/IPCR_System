from django.urls import path
from . import views

urlpatterns = [
    path('IPCR_Form', views.IPCRForm, name = 'IPCR_Form'),
    path('Show_IPCR', views.Show_IPCR, name = 'Show_IPCR'),
]
