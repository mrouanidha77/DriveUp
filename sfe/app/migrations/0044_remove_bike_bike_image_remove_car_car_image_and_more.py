# Generated by Django 5.0.4 on 2024-05-21 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0043_alter_bike_bike_image_alter_car_car_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bike',
            name='bike_image',
        ),
        migrations.RemoveField(
            model_name='car',
            name='car_image',
        ),
        migrations.RemoveField(
            model_name='truck',
            name='truck_image',
        ),
    ]
