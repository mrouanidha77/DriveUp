# Generated by Django 5.0.4 on 2024-04-28 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_otherfields',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='profile_images'),
        ),
    ]
