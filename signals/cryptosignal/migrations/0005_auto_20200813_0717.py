# Generated by Django 3.1 on 2020-08-13 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptosignal', '0004_auto_20200813_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='binarysignal',
            name='Images',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='binarysignal',
            name='TakeProfit2',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='binarysignal',
            name='TakeProfit3',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='binarysignal',
            name='TakeProfit4',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
    ]