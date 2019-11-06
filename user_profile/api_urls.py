from django.urls import path, include
from .api_views import ProfileViewSet, DispatcherViewSet

from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'profiles', ProfileViewSet, 'profiles')
router.register(r'dispatchers', DispatcherViewSet, 'dispatchers')

urlpatterns = [
    path('', include(router.urls)),
]
