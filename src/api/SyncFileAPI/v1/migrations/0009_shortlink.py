# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0008_auto_20150727_0255'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortLink',
            fields=[
                ('id', models.CharField(primary_key=True, max_length=50, serialize=False)),
                ('link', models.CharField(max_length=2000)),
            ],
        ),
    ]
