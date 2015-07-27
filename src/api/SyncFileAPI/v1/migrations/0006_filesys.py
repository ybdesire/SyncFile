# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0005_auto_20150718_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileSys',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('parentid', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=20)),
                ('createdate', models.DateTimeField(blank=True)),
                ('creator', models.CharField(max_length=200)),
                ('filename', models.CharField(max_length=200)),
                ('foldername', models.CharField(max_length=200)),
            ],
        ),
    ]
