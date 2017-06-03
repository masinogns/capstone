# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-03 15:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import menza.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=menza.models.user_path)),
                ('thumnail_image', models.ImageField(blank=True, upload_to='')),
                ('room_phone', models.CharField(max_length=255)),
                ('room_name', models.CharField(max_length=255)),
                ('room_monthly', models.CharField(max_length=255)),
                ('comment', models.CharField(max_length=255)),
                ('upload_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Upload Date')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-upload_date'],
            },
        ),
    ]
