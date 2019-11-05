"""memo URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

from django.shortcuts import redirect


def index(request):
    return redirect('/on/dashboard/')


urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('production/', include('service_note.urls')),
    path('on/', include('on.urls')),
    # path('userprofile/', include('user_profile.urls')),
    path('documents/', include('incoming_documents.urls')),
    # rest
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('api/', include('user_profile.urls')),
    path('api/', include('history.urls')),

]
