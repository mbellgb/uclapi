# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-16 09:45
from __future__ import unicode_literals

import dashboard.app_helpers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_user_agreement'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemporaryToken',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('api_token', models.CharField(default=dashboard.app_helpers.generate_temp_api_token, max_length=1000, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('uses', models.IntegerField(default=0)),
            ],
        ),
    ]
