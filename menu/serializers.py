from rest_framework import serializers
from .models import Reservation, Order


class ReservationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reservation
        fields = ['user', 'url', 'name', 'date', 'time', 'persons_number']
        
        
class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = ['url', 'user', 'dish', 'quantity', 'total_price', 'order_date', 'order_time']
        