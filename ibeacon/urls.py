from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from . import views


urlpatterns = [
    # path('beacons', views.beacons_index),
    path('api/login', views.login),
    path('api/sampleapi', views.sample_api),
    path('api/beacons', views.beacons_index)

]