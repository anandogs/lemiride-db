# Generated by Django 4.0.4 on 2022-05-16 12:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lemiride_app_db', '0023_alter_productdetails_available_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='available_from',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 16, 18, 5, 7, 823376)),
        ),
        migrations.AlterField(
            model_name='transactiondetails',
            name='booking_date',
            field=models.DateField(blank=True, null=True, verbose_name='Booking Date'),
        ),
    ]
