# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 17:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mighty_app', '0004_auto_20160708_1422'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created']},
        ),
    ]
