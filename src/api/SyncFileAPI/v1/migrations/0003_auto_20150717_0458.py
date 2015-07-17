# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0002_usertoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertoken',
            name='authTime',
            field=models.TimeField(blank=True),
        ),
    ]
