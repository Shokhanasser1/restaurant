from django.urls import path, include
from . import views
from .api_views import *

urlpatterns = [
    path('', views.menu, name='menu'),
    path('main_menu/', views.main_menu, name='main_menu'),
    path('add_dish/', views.add_dish, name='add_dish'),
    path('dish/<int:dish_id>/', views.dish_detail, name='dish_detail'),
    path('dish/<int:dish_id>/delete/', views.dish_delete, name='dish_delete'),
    path('order/<int:dish_id>/', views.order_dish, name='order_dish'),
    path('top_dishes/', views.top_dishes_view, name='top_dishes'),
    path('my_orders/', views.user_orders_list, name='my_order_list'),
    path('full_menu/', views.full_menu_view, name='full_menu'),

    path('api-dishes/', DishListCreateAPIView.as_view(), name='api_dishes'),
    path('api-dishes/<int:pk>/', DishRetrieveUpdateDestroyAPIView.as_view(), name='api_dish_detail'),
    path('api-update-dish/<int:pk>/', DishRetrieveUpdateDestroyAPIView.as_view(), name='api-update-dish'),
    path('api-delete-dish/<int:pk>/', DishView.as_view(), name='api-delete-dish'),
]

