# Generated by Django 3.1 on 2020-08-20 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cryptosignal', '0017_auto_20200820_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favlist',
            old_name='binarysignalID',
            new_name='binarysignal',
        ),
    ]
