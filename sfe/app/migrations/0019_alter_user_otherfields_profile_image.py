# Generated by Django 5.0.4 on 2024-04-28 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_user_otherfields_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_otherfields',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='static/profile_images'),
        ),
    ]
