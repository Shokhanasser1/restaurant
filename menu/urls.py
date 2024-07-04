from django.urls import path, include
from . import views
from users.views import *

urlpatterns = [
    path('create/', create_user, name='create_user'),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    
    path('', include('users.urls')),

    path('create_reservation/', views.create_reservation, name='create_reservation'),
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('', views.home, name='home'),
    path('menu/', include('menu.menu_urls')),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]