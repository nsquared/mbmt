# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-18 14:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_auto_20170318_1001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='year',
        ),
        migrations.AddField(
            model_name='competition',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 3, 18, 14, 41, 2, 526170, tzinfo=utc)),
            preserve_default=False,
        ),
    ]