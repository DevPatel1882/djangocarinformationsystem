# Generated by Django 3.1.6 on 2021-02-10 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_data', '0038_auto_20210210_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell_car_details',
            name='phone_num',
            field=models.IntegerField(),
        ),
    ]
