# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 20:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=20)),
                ('note', models.TextField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=4)),
                ('complete', models.BooleanField(default=False)),
                ('paid', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('items', models.ManyToManyField(to='mighty_app.MenuItem')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(choices=[('Cook', 'Cook'), ('Server', 'Server'), ('Owner', 'Owner')], max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
