# Generated by Django 4.2.5 on 2023-11-13 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_remove_movingdata_id_alter_movingdata_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='movingdata',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='movingdata',
            name='count',
            field=models.IntegerField(),
        ),
    ]
