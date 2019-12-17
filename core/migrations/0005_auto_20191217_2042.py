# Generated by Django 2.2.4 on 2019-12-17 17:12

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20191215_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=50, verbose_name='شهر'),
        ),
        migrations.AlterField(
            model_name='city',
            name='ostan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Ostan', verbose_name='استان'),
        ),
        migrations.AlterField(
            model_name='melk',
            name='melk_comment',
            field=ckeditor.fields.RichTextField(max_length=1000, verbose_name='توضیحات سند ملک'),
        ),
        migrations.AlterField(
            model_name='rosta',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.City', verbose_name='شهرستان'),
        ),
    ]