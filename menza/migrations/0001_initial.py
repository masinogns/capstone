# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-03 16:38
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
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('town', models.CharField(max_length=50)),
                ('village', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Option_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parking', models.BooleanField(default=False)),
                ('elevator', models.BooleanField(default=False)),
                ('animal', models.BooleanField(default=False)),
                ('aricon', models.BooleanField(default=False)),
                ('washer', models.BooleanField(default=False)),
                ('freezer', models.BooleanField(default=False)),
                ('tv', models.BooleanField(default=False)),
                ('doorlock', models.BooleanField(default=False)),
                ('bed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=menza.models.user_path)),
                ('thumnail_image', models.ImageField(blank=True, upload_to='')),
                ('room_phone', models.CharField(max_length=255)),
                ('room_name', models.CharField(max_length=255)),
                ('deposit', models.IntegerField(blank=True)),
                ('monthly', models.IntegerField(blank=True)),
                ('manage_money', models.IntegerField(blank=True)),
                ('rome_area', models.IntegerField(blank=True)),
                ('detail_address', models.CharField(max_length=255)),
                ('upload_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Upload Date')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-upload_date'],
            },
        ),
        migrations.AddField(
            model_name='option_info',
            name='rome_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menza.Photo'),
        ),
        migrations.AddField(
            model_name='address',
            name='rome_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menza.Photo'),
        ),
    ]
