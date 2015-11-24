# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_remove_thumbnail_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=120)),
                ('slug', models.SlugField(unique=True)),
                ('active', models.BooleanField(default=True)),
                ('products', models.ManyToManyField(to='products.Product', blank=True)),
            ],
        ),
    ]
