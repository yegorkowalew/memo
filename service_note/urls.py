from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('sn/', views.sn),
    # path('on/', views.on),
    path('ro/', views.ro),
    path('ind/', views.ind),
    path('wb/', views.wb),
    path('filereadadmin/', views.filereadadmin),
    path('filereadadmin/all/', views.filereadadminAll),
]