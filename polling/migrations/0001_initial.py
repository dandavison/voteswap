# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-11 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('updated', models.DateField()),
                ('abbv', models.CharField(max_length=255)),
                ('tipping_point_rank', models.IntegerField()),
                ('safe_for', models.CharField(choices=[('clinton', 'Clinton'), ('johnson', 'Johnson'), ('stein', 'Stein'), ('trump', 'Trump'), ('none', 'No One')], default='none', max_length=255)),
                ('safe_rank', models.IntegerField(default=-1)),
                ('leans', models.CharField(choices=[('clinton', 'Clinton'), ('johnson', 'Johnson'), ('stein', 'Stein'), ('trump', 'Trump'), ('none', 'No One')], default='none', max_length=255)),
                ('lean_rank', models.IntegerField(default=-1)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='state',
            unique_together=set([('name', 'updated')]),
        ),
    ]
