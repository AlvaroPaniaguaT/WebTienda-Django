# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myStore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikes',
            name='b_type',
            field=models.CharField(default='monta\xf1a', max_length=200),
            preserve_default=False,
        ),
    ]
