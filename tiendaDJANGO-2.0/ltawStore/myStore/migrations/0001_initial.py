# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Bikes',
            fields=[
                ('product_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='myStore.Product')),
                ('brand', models.CharField(max_length=200)),
            ],
            bases=('myStore.product',),
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('product_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='myStore.Product')),
                ('author', models.CharField(max_length=200)),
                ('book_genre', models.CharField(max_length=200)),
            ],
            bases=('myStore.product',),
        ),
        migrations.CreateModel(
            name='CD',
            fields=[
                ('product_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='myStore.Product')),
                ('author', models.CharField(max_length=200)),
                ('cd_genre', models.CharField(max_length=200)),
            ],
            bases=('myStore.product',),
        ),
    ]
