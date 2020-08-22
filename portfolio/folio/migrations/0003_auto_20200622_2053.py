# Generated by Django 3.0.6 on 2020-06-22 20:53

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folio', '0002_auto_20200527_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myinfo',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='myinfo',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
