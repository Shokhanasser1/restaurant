from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from . import views
from users.views import *
from menu.api_views import *
from users.api_views import ProfileViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'reservations', ReservationViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'dishes', DishViewSet)
router.register(r'categories', CategoryViewSet)

router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    
    
    
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