# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_remove_thumbnail_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sale_active',
            field=models.BooleanField(default=False),
        ),
    ]
