from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['is_active']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        instance = User.objects.create_user(
            email=validated_data.get('email', None),
            password=validated_data.get('password', None),
            first_name=validated_data.get('first_name', None),
            last_name=validated_data.get('last_name', None),
        )
        instance.save()
        return instance
