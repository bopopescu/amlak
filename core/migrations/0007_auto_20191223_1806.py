# Generated by Django 2.2.4 on 2019-12-23 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20191217_2129'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'شهر', 'verbose_name_plural': 'شهرستان'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': 'موقعیت', 'verbose_name_plural': 'موقعیت جغرافیایی'},
        ),
        migrations.AlterModelOptions(
            name='melk',
            options={'ordering': ['sanad_asli'], 'verbose_name': 'ملک', 'verbose_name_plural': 'املاک'},
        ),
        migrations.AlterModelOptions(
            name='ostan',
            options={'verbose_name': 'استان', 'verbose_name_plural': 'استان ها'},
        ),
        migrations.AlterModelOptions(
            name='rosta',
            options={'verbose_name': 'روستا', 'verbose_name_plural': 'دهستان'},
        ),
        migrations.AlterModelOptions(
            name='unit',
            options={'verbose_name': 'منطقه', 'verbose_name_plural': 'مناطق'},
        ),
    ]