# Generated by Django 3.1.6 on 2021-02-08 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_data', '0033_auto_20210208_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell_car',
            name='images',
            field=models.FileField(default='', upload_to='car_data/sellcar'),
        ),
    ]
