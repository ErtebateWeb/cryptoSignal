# Generated by Django 3.1 on 2020-08-20 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cryptosignal', '0014_auto_20200819_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='binarysignal',
            name='IsActive',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='FavList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SymbolTitle', models.CharField(max_length=30)),
                ('TimeFrame', models.CharField(default='1D', max_length=30)),
                ('NowPrice', models.CharField(max_length=30)),
                ('TriggerPrice', models.CharField(max_length=30)),
                ('StopLoss', models.CharField(max_length=30)),
                ('TakeProfit1', models.CharField(max_length=30)),
                ('TakeProfit2', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('TakeProfit3', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('TakeProfit4', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('LivePrice', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('IsTriggered', models.BooleanField(default=True)),
                ('IsStopLossed', models.BooleanField(default=True)),
                ('IsTP1', models.BooleanField(default=True)),
                ('IsTP2', models.BooleanField(default=True)),
                ('IsTP3', models.BooleanField(default=True)),
                ('IsTP4', models.BooleanField(default=True)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('binarysignalID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cryptosignal.binarysignal')),
            ],
        ),
    ]
