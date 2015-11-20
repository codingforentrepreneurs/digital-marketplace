# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import products.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0013_myproducts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('height', models.CharField(max_length=20, null=True, blank=True)),
                ('width', models.CharField(max_length=20, null=True, blank=True)),
                ('media', models.ImageField(height_field=b'height', width_field=b'width', null=True, upload_to=products.models.download_media_location, blank=True)),
                ('product', models.ForeignKey(to='products.Product')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterModelOptions(
            name='myproducts',
            options={'verbose_name': 'My Products', 'verbose_name_plural': 'My Products'},
        ),
    ]
