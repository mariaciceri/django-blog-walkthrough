# Generated by Django 4.2.17 on 2024-12-29 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='about', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
