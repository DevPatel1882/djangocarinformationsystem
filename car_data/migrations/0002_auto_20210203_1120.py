# Generated by Django 3.1.6 on 2021-02-03 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maruti',
            old_name='model_arena',
            new_name='ex_showroom_price',
        ),
        migrations.RenameField(
            model_name='maruti',
            old_name='model_nexa',
            new_name='model_category',
        ),
    ]
