# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-21 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image_10',
            field=models.ImageField(default=None, upload_to='media/listings/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='image_6',
            field=models.ImageField(default=None, upload_to='media/listings/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='image_7',
            field=models.ImageField(default=None, upload_to='media/listings/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='image_8',
            field=models.ImageField(default=None, upload_to='media/listings/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='image_9',
            field=models.ImageField(default=None, upload_to='media/listings/'),
        ),
    ]
