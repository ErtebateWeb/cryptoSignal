# Generated by Django 3.1 on 2020-08-18 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptosignal', '0010_auto_20200818_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='binarysignal',
            name='Images',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/'),
        ),
    ]
