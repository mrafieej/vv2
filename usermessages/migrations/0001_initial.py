# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-15 00:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('listing', '0001_initial'),
        ('userprofiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(default=None, max_length=2000)),
                ('message_date', models.DateTimeField(default=None)),
                ('is_read', models.BooleanField(default=None)),
                ('listing', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='listing.Listing')),
                ('receiver', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='receiver_user_profile', to='userprofiles.UserProfile')),
                ('sender', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='sender_user_profile', to='userprofiles.UserProfile')),
            ],
        ),
    ]
