from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email']


class UserProfileCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()

    def create(self, validated_data):
        return UserProfile.objects.create(**validated_data)


class UserProfileUpdateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, required=False)
    email = serializers.EmailField(required=False)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
