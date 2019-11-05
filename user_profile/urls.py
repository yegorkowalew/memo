from django.contrib import admin
from django.urls import path, include
from . import views
from .utils import renew_user_from_folder
from .views import ProfileViewSet

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)


# app_name = "user_profile"

urlpatterns = [
    path('adm/renew/', renew_user_from_folder.renew),

    path('', include(router.urls)),
    # path('adm/', utils.ind),
    # path('', views.order_list),
    # path('ro/', views.ro),
    # path('ind/', views.ind),
    # path('wb/', views.wb),
    # path('filereadadmin/', views.filereadadmin),
    # path('filereadadmin/all/', views.filereadadminAll),
]

# from django.urls import include, path
# from rest_framework import routers
# from tutorial.quickstart import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]