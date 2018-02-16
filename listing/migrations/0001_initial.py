# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-15 00:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default=None, max_length=80)),
                ('location', models.CharField(default=None, max_length=30)),
                ('description', models.TextField(default=None)),
                ('bedrooms', models.IntegerField(default=None)),
                ('bathrooms', models.FloatField(default=None)),
                ('capacity', models.IntegerField(default=None)),
                ('square_footage', models.IntegerField(default=None)),
                ('street', models.CharField(default=None, max_length=120)),
                ('city', models.CharField(default=None, max_length=80)),
                ('zip_code', models.IntegerField(default=None)),
                ('cats_ok', models.BooleanField(default=None)),
                ('dogs_ok', models.BooleanField(default=None)),
                ('smoking_ok', models.BooleanField(default=None)),
                ('availability_from', models.DateField(default=None)),
                ('availability_to', models.DateField(default=None)),
                ('points_per_night', models.IntegerField(default=None)),
                ('deposit', models.IntegerField(default=None)),
                ('image_1', models.ImageField(default=None, upload_to='media/listings/')),
                ('image_2', models.ImageField(default=None, upload_to='media/listings/')),
                ('image_3', models.ImageField(default=None, upload_to='media/listings/')),
                ('image_4', models.ImageField(default=None, upload_to='media/listings/')),
                ('image_5', models.ImageField(default=None, upload_to='media/listings/')),
                ('pub_date', models.DateTimeField(default=None)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='userprofiles.UserProfile')),
            ],
        ),
    ]