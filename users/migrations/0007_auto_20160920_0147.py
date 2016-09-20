# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-20 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20160918_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fb_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='second_candidate',
            field=models.CharField(blank=True, choices=[('Clinton', 'Clinton'), ('Johnson', 'Johnson'), ('Stein', 'Stein'), ('Trump', 'Trump')], max_length=255, null=True),
        ),
    ]
