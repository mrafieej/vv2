# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-21 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0002_auto_20180221_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image_10',
            field=models.ImageField(blank=True, default=None, upload_to='media/listings/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image_2',
            field=models.ImageField(blank=True, default=None, upload_to='media/listings/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image_3',
            field=models.ImageField(blank=True, default=None, upload_to='media/listings/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image_4',
            field=models.ImageField(blank=True, default=None, upload_to='media/listings/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image_5',
            field=models.ImageField(blank=True, default=None, upload_to='media/listings/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image_6',
            field=models.ImageField(blank=True, default=None, upload_to='media/listings/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image_7',
            field=models.ImageField(blank=True, default=None, upload_to='media/listings/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image_8',
            field=models.ImageField(blank=True, default=None, upload_to='media/listings/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image_9',
            field=models.ImageField(blank=True, default=None, upload_to='media/listings/'),
        ),
    ]