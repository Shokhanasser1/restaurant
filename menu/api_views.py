from rest_framework import permissions, viewsets, generics
from .serializers import ReservationSerializer, OrderSerializer, DishSerializer, CategorySerializer
from .models import Reservation, Order, Dish, Category
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
    
class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [permissions.AllowAny]

class DishListCreateAPIView(generics.ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class DishRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class DishView(APIView):
    def get(self, request, pk=None):
        context = {'request': request}
        if pk:
            dish = Dish.objects.get(pk=pk)
            dish = DishSerializer(dish, context=context)
            return Response(dish.data, status=status.HTTP_200_OK)

    def post(self, request):
        context = {'request': request}
        data = DishSerializer(data=request.data, context=context)
        
        if data.is_valid():
            data.save()
            
    def put(self, request, pk):
        context = {'request': request}
        dish = Dish.objects.get(id=pk)
        data = DishSerializer(instance=dish, data=request.data, context=context)

        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_200_OK)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        dish = Dish.objects.get(id=pk)
        dish.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]