from django.contrib import admin
from django.urls import path, include
from . import views
from .utils import renew_from_file, renew_ready_from_file, utils


# from rest_framework import routers
# router = routers.DefaultRouter()
# router.register(r'ongraph', views.ongraph, 'ongraph')

urlpatterns = [
    # path('ongraph/', views.ongraph),

    # path('', include(router.urls)),

    path('dashboard/', views.dashboard),
    path('adm/index/', views.adm_index),
    # path('adm/json/', views.jsonreturn),
    path('adm/', utils.ind),
    path('adm/renew/', renew_from_file.renew),
    path('adm/renew-ready/', renew_ready_from_file.renew),
    path('', views.order_list),
]
