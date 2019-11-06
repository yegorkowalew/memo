# from django.contrib import admin
from django.urls import path #, include
# from . import views
from .utils import renew_user_from_folder

urlpatterns = [
    path('adm/renew/', renew_user_from_folder.renew),
    # path('', include(router.urls)),
]
