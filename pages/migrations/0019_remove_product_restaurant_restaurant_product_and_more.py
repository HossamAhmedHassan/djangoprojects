# Generated by Django 5.0 on 2023-12-18 16:43

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_alter_order_date_alter_order_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(auto_created=True, verbose_name=datetime.datetime(2023, 12, 18, 18, 43, 1, 679721)),
        ),
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.TimeField(auto_created=True, verbose_name=datetime.datetime(2023, 12, 18, 18, 43, 1, 679721)),
        ),
    ]
