# Generated by Django 4.2.5 on 2023-11-09 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='photos/%y/%m/%d'),
        ),
    ]
