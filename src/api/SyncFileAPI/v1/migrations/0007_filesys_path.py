# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0006_filesys'),
    ]

    operations = [
        migrations.AddField(
            model_name='filesys',
            name='path',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]
