# Generated by Django 3.1 on 2020-08-13 04:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptosignal', '0005_auto_20200813_0717'),
    ]

    operations = [
        migrations.RenameField(
            model_name='binarysignal',
            old_name='DateCreated',
            new_name='CreatedDate',
        ),
        migrations.AddField(
            model_name='binarysignal',
            name='updatedDate',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
