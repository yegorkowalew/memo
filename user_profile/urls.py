from django.contrib import admin
from django.urls import path, include
from . import views
from .utils import renew_user_from_folder
from .views import ProfileViewSet, DispatcherViewSet

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'dispatchers', views.DispatcherViewSet)


urlpatterns = [
    path('adm/renew/', renew_user_from_folder.renew),
    path('', include(router.urls)),
]
