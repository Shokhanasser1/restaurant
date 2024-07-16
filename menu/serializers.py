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
        fields = ['url', 'id', 'name', 'price', 'image', 'description', 'category']

    def create(self, validated_data):
        return Dish.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.image = validated_data.get('image', instance.image)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance
        
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['url', 'name']