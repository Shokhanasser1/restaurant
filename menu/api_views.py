from rest_framework import permissions, viewsets, generics
from .serializers import ReservationSerializer, OrderSerializer
from .models import Reservation, Order
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.forms.models import model_to_dict
from django.contrib.auth.models import User

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.AllowAny]
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]
    