# Generated by Django 5.0 on 2023-12-17 13:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_cartproduct_order_restaurant_delete_moveddata_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=50, null=True)),
                ('price', models.DecimalField(decimal_places=0, max_digits=5)),
                ('image', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('restaurant', models.CharField(choices=[], max_length=50)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(verbose_name=datetime.datetime(2023, 12, 17, 15, 53, 13, 441805)),
        ),
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.TimeField(verbose_name=datetime.datetime(2023, 12, 17, 15, 53, 13, 442806)),
        ),
    ]