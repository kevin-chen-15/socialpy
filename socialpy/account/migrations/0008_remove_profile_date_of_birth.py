# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20160722_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='date_of_birth',
        ),
    ]
