# Generated by Django 5.0.4 on 2024-05-16 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_remove_part_course_remove_lesson_part_delete_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='vehicle',
            field=models.CharField(choices=[('Voiture', 'Voiture'), ('Moto', 'Moto'), ('Poids Lourd', 'Poids lourd')], max_length=20, null=True),
        ),
    ]
