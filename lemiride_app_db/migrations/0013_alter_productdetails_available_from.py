# Generated by Django 4.0.4 on 2022-05-15 05:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lemiride_app_db', '0012_alter_productdetails_available_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='available_from',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 15, 10, 57, 43, 34891)),
        ),
    ]
