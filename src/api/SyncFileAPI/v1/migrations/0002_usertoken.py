# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('userName', models.CharField(max_length=200)),
                ('authID', models.CharField(max_length=200)),
                ('authTime', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
