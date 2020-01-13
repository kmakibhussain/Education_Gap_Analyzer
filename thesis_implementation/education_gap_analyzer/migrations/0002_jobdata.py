# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-30 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education_gap_analyzer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='jobData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobTitle', models.CharField(max_length=70)),
                ('category', models.CharField(max_length=40)),
                ('jobReuirments', models.TextField()),
                ('relatedDept', models.CharField(max_length=50)),
                ('keywords', models.TextField()),
            ],
        ),
    ]
