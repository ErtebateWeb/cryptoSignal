# Generated by Django 3.1 on 2020-08-12 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='binarysignal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SymbolTitle', models.CharField(max_length=30)),
                ('NowPrice', models.CharField(max_length=30)),
                ('StopLoss', models.CharField(max_length=30)),
                ('TriggerPrice', models.CharField(max_length=30)),
                ('TakeProfit1', models.CharField(max_length=30)),
                ('TakeProfit2', models.CharField(max_length=30, null=True)),
                ('TakeProfit3', models.CharField(max_length=30, null=True)),
                ('TakeProfit4', models.CharField(max_length=30, null=True)),
                ('DateCreated', models.CharField(max_length=30)),
                ('Publisher', models.CharField(max_length=30)),
                ('Images', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
