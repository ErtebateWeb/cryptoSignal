# Generated by Django 3.1 on 2020-08-20 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cryptosignal', '0016_auto_20200820_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favlist',
            name='NowPrice',
        ),
        migrations.RemoveField(
            model_name='favlist',
            name='StopLoss',
        ),
        migrations.RemoveField(
            model_name='favlist',
            name='TakeProfit1',
        ),
        migrations.RemoveField(
            model_name='favlist',
            name='TakeProfit2',
        ),
        migrations.RemoveField(
            model_name='favlist',
            name='TakeProfit3',
        ),
        migrations.RemoveField(
            model_name='favlist',
            name='TakeProfit4',
        ),
        migrations.RemoveField(
            model_name='favlist',
            name='TimeFrame',
        ),
        migrations.RemoveField(
            model_name='favlist',
            name='TriggerPrice',
        ),
    ]
