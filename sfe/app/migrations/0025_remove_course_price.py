# Generated by Django 5.0.4 on 2024-05-03 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_remove_course_is_purchassed_delete_coursepurchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='price',
        ),
    ]