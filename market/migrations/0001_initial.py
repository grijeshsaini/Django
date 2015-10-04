# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('brand_id', models.AutoField(serialize=False, primary_key=True)),
                ('brand_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_id', models.BigIntegerField(unique=True, verbose_name=b'category_id')),
                ('category_name', models.CharField(max_length=200)),
                ('username', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=b'username')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_id', models.BigIntegerField(unique=True)),
                ('item_name', models.CharField(max_length=200)),
                ('sub_category', models.ForeignKey(to='market.Category', to_field=b'category_id')),
                ('username', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=b'username')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.ForeignKey(to='market.Item', to_field=b'item_id')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('status_id', models.IntegerField(serialize=False, primary_key=True)),
                ('status_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionDetails',
            fields=[
                ('transaction_id', models.AutoField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='transaction',
            field=models.ForeignKey(to='market.TransactionDetails'),
        ),
        migrations.AddField(
            model_name='order',
            name='username',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=b'username'),
        ),
    ]
