from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ['url', 'id', 'user', 'first_name', 'last_name', 'email', 'bio']