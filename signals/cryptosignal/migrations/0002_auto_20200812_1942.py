# Generated by Django 3.1 on 2020-08-12 15:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptosignal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='binarysignal',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='binarysignal',
            name='Images',
            field=models.ImageField(default='', null=True, upload_to='images/'),
        ),
    ]
