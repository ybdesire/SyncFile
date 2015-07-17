# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0003_auto_20150717_0458'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAuthID',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('userName', models.CharField(max_length=200)),
                ('authID', models.CharField(max_length=50)),
                ('authTime', models.TimeField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='UserToken',
        ),
    ]
