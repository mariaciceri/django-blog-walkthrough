# Generated by Django 4.2.17 on 2025-01-01 14:23

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_collaboraterequest_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collaboraterequest',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='about',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]