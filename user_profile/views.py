from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

# from django.contrib.auth.models import User, Group
from .models import Profile
from rest_framework import viewsets
from .serializers import ProfileSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('user_no')
    serializer_class = ProfileSerializer