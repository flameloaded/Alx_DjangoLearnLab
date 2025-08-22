from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        # Explicitly using get_user_model().objects.create_user (not User.objects.create_user)
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # Explicitly using Token.objects.create
        Token.objects.create(user=user)
        return user
