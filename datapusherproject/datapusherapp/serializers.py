from .models import DestinationModel, RoleModel, LogModel, AccountMemberModel, AccountModel
from rest_framework import serializers
from django.contrib.auth.models import User

# Role Model Serializer
class RoleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleModel
        fields = '__all__'
        
# Account Model Serializer
class AccountModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        fields = '__all__'
        
# Account Member Model Serializer
class AccountMemberModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountMemberModel
        fields = '__all__'
        
# Destination Model Serializer
class DestinationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationModel
        fields = '__all__'
        
# Log Model Serializer
class LogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogModel
        fields = '__all__'
        
# Register Serializer

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# Login Serializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
