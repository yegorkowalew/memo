"""memo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
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

]
