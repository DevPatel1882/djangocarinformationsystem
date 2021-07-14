# Generated by Django 3.1.6 on 2021-02-10 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_data', '0036_auto_20210208_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sell_Car_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone_num', models.IntegerField(max_length=10)),
                ('state', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=6)),
                ('address', models.TextField()),
                ('car_company', models.CharField(max_length=100)),
                ('car_year', models.CharField(max_length=100)),
                ('car_model', models.CharField(max_length=200)),
                ('kms_driven', models.CharField(max_length=200)),
                ('car_ownership', models.CharField(max_length=300)),
                ('Expected_price', models.CharField(max_length=200)),
                ('car_img', models.ImageField(upload_to='car_data/sell_car_img')),
            ],
        ),
    ]
