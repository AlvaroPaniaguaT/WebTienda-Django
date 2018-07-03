# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myStore', '0002_bikes_b_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default=b'', max_length=1000),
        ),
        migrations.AddField(
            model_name='product',
            name='external_url',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
