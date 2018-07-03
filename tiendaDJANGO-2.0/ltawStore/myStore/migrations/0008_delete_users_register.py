# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myStore', '0007_users_register'),
    ]

    operations = [
        migrations.DeleteModel(
            name='users_register',
        ),
    ]
