# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-04 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
        ('candidates', '0004_auto_20210304_2225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='skills',
        ),
        migrations.AddField(
            model_name='candidate',
            name='skills',
            field=models.ManyToManyField(to='skills.Skill'),
        ),
    ]
