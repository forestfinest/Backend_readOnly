# Generated by Django 3.1.1 on 2021-02-05 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.CharField(max_length=50, null=True),
        ),
    ]