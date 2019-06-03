# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-30 08:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('title', models.CharField(blank=True, max_length=31)),
                ('posted_by', models.CharField(blank=True, max_length=50)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True)),
                ('technologies', models.CharField(blank=True, max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clone.User')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', pyuploadcare.dj.models.ImageField(blank=True)),
                ('bio', models.CharField(default='Hi!', max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='clone.User')),
            ],
        ),
    ]
