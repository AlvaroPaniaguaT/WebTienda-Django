# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myStore', '0005_buyorders'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyorders',
            name='confirmed',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
