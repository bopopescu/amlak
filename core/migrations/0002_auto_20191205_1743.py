# Generated by Django 2.2.4 on 2019-12-05 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='city',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='ostan',
            old_name='ostan',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='rosta',
            old_name='rosta',
            new_name='name',
        ),
    ]