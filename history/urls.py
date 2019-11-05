# from django.contrib import admin
from django.urls import path, include
from . import views
# from .utils import renew_user_from_folder
from .views import HistoryViewSet

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'history', views.HistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('filereadadmin/all/', views.filereadadminAll),
]
