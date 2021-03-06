# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-15 00:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.CharField(default=None, max_length=100)),
                ('password', models.CharField(default=None, max_length=100)),
                ('firstname', models.CharField(default=None, max_length=100)),
                ('lastname', models.CharField(default=None, max_length=100)),
                ('location', models.CharField(default=None, max_length=100)),
                ('occupation', models.CharField(default=None, max_length=100)),
                ('about', models.TextField(default=None, max_length=1000)),
                ('profile_pic', models.ImageField(default=None, upload_to='media/profile_pics/')),
                ('points', models.IntegerField(default=None)),
                ('last_logged', models.DateTimeField(default=None)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
