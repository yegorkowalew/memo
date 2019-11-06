from django.urls import path, include
from .api_views import HistoryViewSet

from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'history', HistoryViewSet, 'history')

urlpatterns = [
    path('', include(router.urls)),
]