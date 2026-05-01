from rest_framework import serializers
from . models import CustomUserModel

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUserModel
        fields = [
            'email', 'password', 'password2',
            'first_name', 'last_name', 'phone_number', 'role',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'role': {'required': False},
        }

    def validate_email(self, value):
        if CustomUserModel.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password2": "Passwords do not match"})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        return CustomUserModel.objects.create_user(**validated_data)

class LoginSerilizer(serializers.Serializer):
    email=serializers.CharField()        
    password=serializers.CharField(write_only=True)  