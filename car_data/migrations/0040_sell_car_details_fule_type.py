# Generated by Django 3.1.6 on 2021-02-10 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_data', '0039_auto_20210210_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell_car_details',
            name='fule_type',
            field=models.CharField(default='', max_length=200),
        ),
    ]
