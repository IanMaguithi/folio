# Generated by Django 3.0.6 on 2020-05-30 16:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof_image', models.ImageField(upload_to='profile images')),
                ('name', models.CharField(max_length=50)),
                ('work', models.CharField(max_length=25)),
                ('birthday', models.DateTimeField()),
                ('website', models.CharField(max_length=110)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=60)),
                ('location', models.CharField(max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=14, validators=[django.core.validators.RegexValidator(message="phone number must be entered in the format:'+2547*******'", regex='^\\+?1?\\d{9,15}?$')])),
            ],
        ),
    ]