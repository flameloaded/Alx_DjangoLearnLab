from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # ALX requires this line

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # ALX requires get_user_model().objects.create_user
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # ALX requires Token.objects.create
        Token.objects.create(user=user)
        return user
