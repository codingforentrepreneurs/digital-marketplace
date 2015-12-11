# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0022_productrating'),
    ]

    operations = [
        migrations.CreateModel(
            name='CuratedProducts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('section_name', models.CharField(max_length=120)),
                ('active', models.BooleanField(default=True)),
                ('products', models.ManyToManyField(to='products.Product', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
