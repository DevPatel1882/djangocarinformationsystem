# Generated by Django 3.1.6 on 2021-02-08 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_data', '0035_auto_20210208_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell_car',
            name='images',
            field=models.ImageField(default='', upload_to='car_data/sellcar'),
        ),
    ]
