from rest_framework.relations import PrimaryKeyRelatedField
from .models import Room, Message
from rest_framework import serializers


# Create a Room Serializer
class RoomSerializer (serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'room']


# Create a Message Serializer
class MessageSerializer (serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'value', 'date', 'user', 'room']