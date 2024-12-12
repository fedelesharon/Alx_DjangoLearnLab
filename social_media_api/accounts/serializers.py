from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token, serializers charField(), Token.objects.create, "get_user_model().objects.create_user"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'profile_picture', 'followers']
