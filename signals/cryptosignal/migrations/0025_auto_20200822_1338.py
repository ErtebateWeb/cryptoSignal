# Generated by Django 3.1 on 2020-08-22 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptosignal', '0024_auto_20200820_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='binarysignal',
            name='Publisher',
            field=models.CharField(choices=[('Secret_army', 'Secret_army'), ('mhfateminia', 'mhfateminia'), ('peyman_gh', 'peyman_gh'), ('Eslaaamiii', 'Eslaaamiii'), ('Reza_Esfilar', 'Reza_Esfilar')], max_length=30),
        ),
    ]
