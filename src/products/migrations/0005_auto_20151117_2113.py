# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20151114_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=b'slug-field'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(default=9.99, null=True, max_digits=100, decimal_places=2),
        ),
    ]
