# Generated by Django 4.2.5 on 2023-11-13 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movingdata',
            name='id',
        ),
        migrations.AlterField(
            model_name='movingdata',
            name='count',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
