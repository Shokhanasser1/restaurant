from rest_framework import serializers
from .models import Reservation, Order, Dish, Category

DISCOUNT_IN_PERSENT = 10

class ReservationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reservation
        fields = ['url', 'user', 'name', 'date', 'time', 'persons_number']
        
        
class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = ['url', 'user', 'dish', 'quantity', 'total_price', 'order_date', 'order_time']
        
class DishSerializer(serializers.ModelSerializer):
    price_in_discount = serializers.SerializerMethodField()
    
    class Meta:
        model = Dish
        fields = ['url', 'id', 'name', 'price_in_discount', 'image', 'description', 'category']

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
        
    def get_price_in_discount(self, obj):
        if obj.discount_percent > 0:
            discount_price = obj.price_after_discount()
            return f'${discount_price:.2f} - ({obj.discount_percent}% discount)'
        return f'${obj.price:.2f}'

    
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['url', 'name']