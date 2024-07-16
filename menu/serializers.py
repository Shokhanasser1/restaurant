from rest_framework import serializers
from .models import Reservation, Order, Dish, Category


class ReservationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reservation
        fields = ['user', 'url', 'name', 'date', 'time', 'persons_number']
        
        
class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = ['url', 'user', 'dish', 'quantity', 'total_price', 'order_date', 'order_time']
        
class DishSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Dish
        fields = ['url', 'name', 'price', 'image', 'description']
        
        
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['url', 'name']