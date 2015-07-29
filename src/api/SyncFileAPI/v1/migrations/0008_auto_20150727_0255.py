# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0007_filesys_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filesys',
            name='filename',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='filesys',
            name='foldername',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
