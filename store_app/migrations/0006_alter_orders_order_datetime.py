# Generated by Django 4.1.4 on 2023-01-28 14:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0005_alter_orders_order_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 28, 17, 26, 48, 962092)),
        ),
    ]
