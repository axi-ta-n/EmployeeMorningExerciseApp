from django.urls import path
from . import views

urlpatterns = [
    path('', views.scan_page, name='scan_page'), 
    path('scan/', views.scan_employee, name='scan_employee'), 
]