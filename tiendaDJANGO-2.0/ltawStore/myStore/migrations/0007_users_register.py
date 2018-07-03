# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myStore', '0006_buyorders_confirmed'),
    ]

    operations = [
        migrations.CreateModel(
            name='users_register',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.PositiveIntegerField()),
            ],
        ),
    ]
