# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market', '0002_auto_20151002_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryMst',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_id', models.BigIntegerField(unique=True, verbose_name=b'category_id')),
                ('category_name', models.CharField(max_length=200)),
                ('parent_id', models.BigIntegerField(default=0, verbose_name=b'parent_id')),
            ],
        ),
        migrations.CreateModel(
            name='DisabledCategories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.ForeignKey(to='market.CategoryMst', to_field=b'category_id')),
                ('username', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=b'username')),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='status_id',
        ),
        migrations.RemoveField(
            model_name='category',
            name='username',
        ),
        migrations.AlterField(
            model_name='item',
            name='sub_category',
            field=models.ForeignKey(to='market.CategoryMst', to_field=b'category_id'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
