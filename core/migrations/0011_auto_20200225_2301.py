# Generated by Django 2.2.4 on 2020-02-25 19:31

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200223_1305'),
    ]

    operations = [
        
        migrations.AddField(
            model_name='melk',
            name='latitude',
            field=models.DecimalField(decimal_places=17, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='melk',
            name='longitude',
            field=models.DecimalField(decimal_places=17, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='melk',
            name='rosta',
            field=models.CharField(default=1, max_length=30, verbose_name='روستا'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='melk',
            name='melk_gps',
            field=location_field.models.plain.PlainLocationField(max_length=63, verbose_name='موقعیت جغرافیایی ملک'),
        ),
        
    ]
