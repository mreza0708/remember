from django.contrib.auth import authenticate
from rest_framework import serializers

from users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('email', 'password', 'name')
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
class LoginSerializer(serializers.Serializer):
        email = serializers.EmailField()
        password = serializers.CharField(write_only=True)

        def validate(self, data):
            user = authenticate(**data)
            if user and user.is_active:
                return user
            raise serializers.ValidationError("Invalid credentials")

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name']
        read_only_fields = ['email']  # Usually email is not editable
