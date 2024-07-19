from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate

from rest_framework import permissions, viewsets, generics
from .serializers import ProfileSerializer
from .models import Profile
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.forms.models import model_to_dict

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=200)
    else:
        return Response({'error': 'Wrong credentials'}, status=400)
    
    
@api_view 
def is_admin(request):
    if request.user.groups.filter(name='admin').exists():
        return Response({'message': 'You are admin'}, status=200)
    else:
        return Response({'message': 'You are not admin'}, status=400)    
