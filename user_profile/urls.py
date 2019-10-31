from django.contrib import admin
from django.urls import path, include
from . import views
# from .utils import renew_from_file, utils
from .utils import renew_user_from_folder

urlpatterns = [
    path('adm/renew/', renew_user_from_folder.renew),
    # path('adm/', utils.ind),
    # path('', views.order_list),
    # path('ro/', views.ro),
    # path('ind/', views.ind),
    # path('wb/', views.wb),
    # path('filereadadmin/', views.filereadadmin),
    # path('filereadadmin/all/', views.filereadadminAll),
]