# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [(b'products', '0001_initial'), (b'products', '0002_remove_product_description'), (b'products', '0003_product_description')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('price', models.DecimalField(default=9.99, max_digits=100, decimal_places=2)),
                ('description', models.TextField(default='Default value')),
            ],
        ),
    ]
