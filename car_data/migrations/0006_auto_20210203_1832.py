# Generated by Django 3.1.6 on 2021-02-03 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_data', '0005_auto_20210203_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='maruti_arena',
            name='first_img',
            field=models.ImageField(default='', upload_to='car_data/images'),
        ),
        migrations.AddField(
            model_name='maruti_arena',
            name='reviews',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='maruti_arena',
            name='second_img',
            field=models.ImageField(default='', upload_to='car_data/images'),
        ),
        migrations.AddField(
            model_name='maruti_arena',
            name='specs_features_and_price',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='maruti_arena',
            name='third_img',
            field=models.ImageField(default='', upload_to='car_data/images'),
        ),
    ]
