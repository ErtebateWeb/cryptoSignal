# Generated by Django 3.1 on 2020-08-20 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cryptosignal', '0023_auto_20200820_1609'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favlist',
            old_name='User_id',
            new_name='User',
        ),
    ]
