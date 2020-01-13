# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-03 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityCurriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('universityName', models.CharField(max_length=50)),
                ('deptName', models.CharField(max_length=50)),
                ('courseName', models.CharField(max_length=50)),
                ('courseContent', models.TextField()),
                ('courseKeyword', models.TextField(null=True)),
            ],
        ),
    ]
