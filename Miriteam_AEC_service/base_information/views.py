from django.contrib.auth.models import User
from rest_framework import generics, permissions

from base_information.models import Event, Program
from base_information.serializers import EventSerializer, ProgramSerializer, UserSerializer


# Create your views here.

class EventsListCreateView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class ProgramListView(generics.ListAPIView):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
