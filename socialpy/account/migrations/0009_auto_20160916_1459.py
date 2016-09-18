# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import account.models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_remove_profile_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default=b'default/default.jpg', upload_to=account.models.user_directory_path),
        ),
    ]
