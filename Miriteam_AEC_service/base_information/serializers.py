from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Event, Program


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'


class ProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = Program
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']
