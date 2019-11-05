from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import History
from rest_framework import viewsets
from .serializers import HistorySerializer

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all().order_by('-pk')
    serializer_class = HistorySerializer