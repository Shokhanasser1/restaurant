from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('main_menu/', views.main_menu, name='main_menu'),
]