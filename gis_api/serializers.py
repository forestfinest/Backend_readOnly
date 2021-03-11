from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from .models import  project_area

class project_area_(GeoFeatureModelSerializer):

	class Meta:
		model = project_area
		fields = ('project','user')
		geo_field = 'geom'