# Generated by Django 5.0 on 2024-06-28 16:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0030_rename_averge_product_price_restaurant_average_product_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateField(editable=False, null=True, verbose_name=datetime.datetime(2024, 6, 28, 19, 52, 41, 952633)),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='average_product_price',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]