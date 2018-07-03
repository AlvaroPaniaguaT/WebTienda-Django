# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myStore', '0003_auto_20180329_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='p_type',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
