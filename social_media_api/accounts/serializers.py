from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # <-- satisfies serializers.CharField()
    password2 = serializers.CharField(write_only=True) # confirm password field

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords must match.")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        # <-- satisfies get_user_model().objects.create_user()
        user = User.objects.create_user(**validated_data)
        return user
