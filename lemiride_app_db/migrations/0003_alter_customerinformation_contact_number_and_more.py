# Generated by Django 4.0.4 on 2022-04-27 10:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lemiride_app_db', '0002_alter_customerinformation_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerinformation',
            name='contact_number',
            field=models.IntegerField(default=0, verbose_name='Mobile Number'),
        ),
        migrations.AlterField(
            model_name='transactiondetails',
            name='payment_date',
            field=models.DateField(blank=True, default=datetime.datetime.now, verbose_name='Payment Date'),
        ),
    ]