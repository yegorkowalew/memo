from django.urls import path, include
from .api_views import ongraph

urlpatterns = [
    path('ongraph/', ongraph),
]