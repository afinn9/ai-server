from rest_framework.serializers import ModelSerializer
from .models import BlacklistedToken, User


class BlacklistedAccessTokenSerializer(ModelSerializer):
    class Meta:
        model = BlacklistedToken
        fields = ['token']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
