# Generated by Django 3.1.6 on 2021-02-10 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_data', '0037_sell_car_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell_car_details',
            name='phone_num',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sell_car_details',
            name='pincode',
            field=models.CharField(max_length=10),
        ),
    ]
