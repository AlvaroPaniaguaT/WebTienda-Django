# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myStore', '0004_product_p_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyOrders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('product_n', models.CharField(max_length=200)),
                ('quantity', models.PositiveIntegerField()),
                ('total_price', models.PositiveIntegerField()),
                ('payMeth', models.CharField(max_length=200)),
                ('full_name', models.CharField(max_length=200)),
                ('email_address', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('add_comments', models.CharField(max_length=200)),
            ],
        ),
    ]
