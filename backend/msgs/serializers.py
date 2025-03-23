from rest_framework import serializers
from .models import Msg


class MsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Msg
        fields = '__all__'


class MsgCreateSerializer(serializers.Serializer):
    slug = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=500, required=False)
    sensor_id = serializers.IntegerField()
    sensor_name = serializers.CharField(max_length=255)
    value = serializers.FloatField()

    def create(self, validated_data):
        return Msg.objects.create(**validated_data)


class MsgUpdateSerializer(serializers.Serializer):
    slug = serializers.CharField(max_length=255, required=False)
    description = serializers.CharField(max_length=500, required=False)
    sensor_id = serializers.IntegerField(required=False)
    sensor_name = serializers.CharField(max_length=255, required=False)
    value = serializers.FloatField(required=False)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
