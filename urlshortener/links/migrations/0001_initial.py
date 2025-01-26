# Generated by Django 5.1.5 on 2025-01-26 20:15

import django.db.models.deletion
import links.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField()),
                ('short_id', models.CharField(default=links.models.generate_short_id, max_length=8, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_accessed', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
