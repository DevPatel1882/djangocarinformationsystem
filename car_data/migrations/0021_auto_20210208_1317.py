# Generated by Django 3.1.6 on 2021-02-08 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_data', '0020_auto_20210208_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell_car',
            name='image',
            field=models.ImageField(default='', upload_to='sellcar_upload'),
        ),
    ]
