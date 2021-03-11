from rest_framework import serializers
from .models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name','company','position','email','password')        

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name','company','position','email','password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['name'], 
            validated_data['company'],
            validated_data['position'], 
            validated_data['email'], 
            validated_data['password']
            )
        return user

class GetDataUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('id', 'name','email','company','position')
