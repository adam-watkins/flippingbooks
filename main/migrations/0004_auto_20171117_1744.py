# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-18 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20171117_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='BookCondition',
            field=models.CharField(choices=[('Used', 'Used'), ('New', 'New'), ('Poor', 'Poor')], max_length=40),
        ),
    ]
