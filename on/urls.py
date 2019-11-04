from django.contrib import admin
from django.urls import path, include
from . import views
from .utils import renew_from_file, renew_ready_from_file, utils

urlpatterns = [
    path('dashboard/', views.dashboard),
    path('adm/index/', views.adm_index),

    path('adm/', utils.ind),
    path('adm/renew/', renew_from_file.renew),
    path('adm/renew-ready/', renew_ready_from_file.renew),
    path('', views.order_list),
]
