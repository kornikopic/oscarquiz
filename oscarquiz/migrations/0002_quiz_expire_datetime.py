# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oscarquiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='expire_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
