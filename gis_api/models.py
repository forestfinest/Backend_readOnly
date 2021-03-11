from django.db import models
from django.contrib.gis.db import models

class project_area(models.Model):
    geom = models.GeometryField(blank=True, null=True)
    id_0 = models.CharField(max_length=255, blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    project = models.CharField(max_length=255, blank=True, null=True)
    projectid = models.IntegerField() 

    class Meta:
        managed = True
        db_table = 'project_area_demo'
