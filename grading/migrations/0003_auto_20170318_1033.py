# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-18 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grading', '0002_auto_20170318_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='round',
            name='ref',
            field=models.CharField(default=0, max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='round',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
