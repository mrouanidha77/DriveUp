# Generated by Django 5.0.4 on 2024-05-22 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0044_remove_bike_bike_image_remove_car_car_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='level',
            field=models.CharField(choices=[('Debutant', 'Debutant'), ('Intermidiare', 'Intermidiare'), ('Avance', 'Avance')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='level',
            field=models.CharField(choices=[('Debutant', 'Debutant'), ('Intermidiare', 'Intermidiare'), ('Avance', 'Avance')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='truck',
            name='level',
            field=models.CharField(choices=[('Debutant', 'Debutant'), ('Intermidiare', 'Intermidiare'), ('Avance', 'Avance')], max_length=20, null=True),
        ),
    ]
