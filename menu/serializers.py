from rest_framework import serializers
from .models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reservation
        fields = ['user', 'url', 'name', 'date', 'time', 'persons_number']