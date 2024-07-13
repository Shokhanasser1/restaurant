from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('main_menu/', views.main_menu, name='main_menu'),
    path('add_dish/', views.add_dish, name='add_dish'),
    path('dish/<int:dish_id>/delete/', views.dish_delete, name='dish_delete'),
    path('dish/<int:dish_id>/', views.dish_detail, name='dish_detail'),
    path('order/<int:dish_id>/', views.order_dish, name='order_dish'),
    path('popular/', views.popular_dishes, name='popular_dishes'),
    path('top_dishes/', views.top_dishes_view, name='top_dishes'),
    
    path('my_orders/', views.user_orders_list, name='my_order_list'),
    
]

