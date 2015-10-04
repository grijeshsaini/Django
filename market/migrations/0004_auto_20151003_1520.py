# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market', '0003_auto_20151003_0738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='username',
        ),
        migrations.AddField(
            model_name='transactiondetails',
            name='username',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=b'NULL', to_field=b'username'),
        ),
    ]
