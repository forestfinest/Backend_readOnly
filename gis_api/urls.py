
#src/gis_rest_project/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views


urlpatterns = [
    path('gis/projects', views.project_area_view.as_view({'get': 'list'}), name='projects'),
    ]