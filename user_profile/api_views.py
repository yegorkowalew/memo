from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile
from rest_framework import viewsets
from .serializers import ProfileSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('user_no')
    serializer_class = ProfileSerializer

class DispatcherViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.exclude(user_no=None)
    serializer_class = ProfileSerializer