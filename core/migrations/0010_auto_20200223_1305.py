# Generated by Django 2.2.4 on 2020-02-23 09:35

import django.contrib.gis.geos.point
from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200223_1055'),
    ]

    operations = [
       
        migrations.AlterField(
            model_name='melk',
            name='melk_gps',
            field=location_field.models.plain.PlainLocationField(default=django.contrib.gis.geos.point.Point(59.0, 36.0), max_length=63, verbose_name='موقعیت جغرافیایی ملک'),
        ),
       
    ]
