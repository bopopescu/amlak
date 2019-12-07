# Generated by Django 2.2.4 on 2019-12-06 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191205_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='melk',
            name='melk_pic',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='تصویر سند ملک'),
        ),
        migrations.AlterField(
            model_name='melk',
            name='sanad_type',
            field=models.CharField(choices=[('عادی', 'عادی'), ('قطعی دفترچه ای', 'قطعی دفترچه ای'), ('قطعی غیرمنقول', 'قطعی غیرمنقول'), ('صلح نامه', 'صلح نامه'), ('وقف نامه', 'وقف نامه'), ('ابتیاعی', 'ابتیاعی')], max_length=50, verbose_name='نوع سند واگذاری'),
        ),
    ]