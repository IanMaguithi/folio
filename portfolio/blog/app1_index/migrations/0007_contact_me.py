# Generated by Django 3.0.6 on 2020-06-03 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1_index', '0006_auto_20200601_2334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_me',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=70)),
                ('message', models.TextField(max_length=700)),
                ('sent_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]