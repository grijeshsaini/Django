# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent_id',
            field=models.BigIntegerField(default=0, verbose_name=b'parent_id'),
        ),
        migrations.AddField(
            model_name='category',
            name='status_id',
            field=models.ForeignKey(default=1, to='market.Status'),
        ),
        migrations.AddField(
            model_name='item',
            name='brand_id',
            field=models.IntegerField(default=0, verbose_name=b'brand_id'),
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.DecimalField(default=0, verbose_name=b'price', max_digits=20, decimal_places=5),
        ),
        migrations.AddField(
            model_name='item',
            name='qty',
            field=models.IntegerField(default=1, verbose_name=b'qty'),
        ),
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.DecimalField(default=0, verbose_name=b'price', max_digits=20, decimal_places=5),
        ),
        migrations.AddField(
            model_name='order',
            name='qty',
            field=models.IntegerField(default=1, verbose_name=b'qty'),
        ),
        migrations.AddField(
            model_name='transactiondetails',
            name='transaction_amount',
            field=models.DecimalField(default=0, verbose_name=b'transaction_amount', max_digits=20, decimal_places=5),
        ),
        migrations.AddField(
            model_name='transactiondetails',
            name='transaction_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 2, 15, 39, 1, 190919, tzinfo=utc), verbose_name=b'transaction_date'),
            preserve_default=False,
        ),
    ]
