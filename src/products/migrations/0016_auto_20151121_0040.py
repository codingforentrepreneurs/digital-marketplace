# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20151121_0005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thumbnail',
            name='hd',
        ),
        migrations.AddField(
            model_name='thumbnail',
            name='title',
            field=models.CharField(default=b'hd', max_length=120),
        ),
    ]
