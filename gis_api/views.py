from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.gis.geos import GEOSGeometry,Point
from . models import  project_area
from . serializers import  project_area_
from rest_framework import permissions

class project_area_view(viewsets.ModelViewSet):
    serializer_class = project_area_
    queryset = project_area.objects.all()
