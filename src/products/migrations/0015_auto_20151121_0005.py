# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20151120_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='thumbnail',
            name='hd',
            field=models.ImageField(null=True, upload_to=products.models.thumbnail_location, blank=True),
        ),
        migrations.AlterField(
            model_name='thumbnail',
            name='media',
            field=models.ImageField(height_field=b'height', width_field=b'width', null=True, upload_to=products.models.thumbnail_location, blank=True),
        ),
    ]
