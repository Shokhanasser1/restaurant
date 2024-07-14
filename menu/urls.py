from django.urls import path, include
from . import views
from users.views import *
from menu.api_views import *

from rest_framework import routers
router = routers.DefaultRouter()

router.register(r'reservations', ReservationViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'dishes', DishViewSet)


urlpatterns = [
    path('create/', create_user, name='create_user'),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    
    path('', views.home, name='home'),
    path('', include('users.urls')),

    path('create_reservation/', views.create_reservation, name='create_reservation'),
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('reservation/<int:reservation_id>/delete/', views.reservation_delete, name='reservation_delete'),
    
    path('order/<int:dish_id>/', views.order_dish, name='order_dish'),
    path('my_orders/', views.user_orders_list, name='user_orders_list'),
    
    
    path('menu/', include('menu.menu_urls')),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
    path('apis/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]