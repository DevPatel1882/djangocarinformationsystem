# Generated by Django 3.1.6 on 2021-02-08 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_data', '0029_auto_20210208_1423'),
    ]

    operations = [
        migrations.DeleteModel(
            name='upload',
        ),
        migrations.AlterField(
            model_name='sell_car',
            name='image',
            field=models.ImageField(upload_to='car_data/images/sellcar'),
        ),
    ]
