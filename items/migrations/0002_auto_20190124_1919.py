# Generated by Django 2.1.4 on 2019-01-24 19:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='bathrooms',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='list_date',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 1, 24, 19, 19, 34, 431713)),
        ),
    ]
