# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 01:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mighty_app', '0002_auto_20160707_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='server',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]