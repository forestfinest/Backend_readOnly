# Generated by Django 3.1.1 on 2021-02-12 09:14

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project_area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('id_0', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('project', models.CharField(blank=True, max_length=255, null=True)),
                ('projectid', models.IntegerField()),
            ],
            options={
                'db_table': 'project_area_demo',
                'managed': False,
            },
        ),
    ]
