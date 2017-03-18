# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-18 14:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_team_competition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='competition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='frontend.Competition'),
        ),
    ]
